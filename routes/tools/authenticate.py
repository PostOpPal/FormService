import functools
from flask import request
from configs.configs import jwtConfig, tokensConfig
from models.generated_models.tokens.user_auth_token import UserAuthToken
import jwt
import os
import time

def authenticate():
    def decorator(funct):
        @functools.wraps(funct)
        def wrapper(*args, **kwargs):
            token = request.headers.get(jwtConfig.jwt_header_key) 
            decoded_jwt = jwt.decode(token, os.environ.get("JWT_SECRET"),
                algorithms=[jwtConfig.jwt_algorithm]) 
            userAuthToken = UserAuthToken(decoded_jwt)
            print(userAuthToken)
            if userAuthToken.type != tokensConfig.auth_token:
                return "Invalid Token", 400
            if int(userAuthToken.expiry) < int(time.time()): 
                return "Expired Token", 400
            return funct(userAuthToken.user_id, userAuthToken.surgery_id, *args, **kwargs)
        return wrapper
    return decorator