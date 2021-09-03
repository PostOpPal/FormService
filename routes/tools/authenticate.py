import functools
from flask import request
from configs.configs import jwtConfig, tokensConfig
from models.generated_models.tokens.user_auth_token import UserAuthToken
from models.generated_models.tokens.doctor_user_auth_token import DoctorUserAuthToken
import jwt
import os
import time

def authenticate():
    def decorator(funct):
        @functools.wraps(funct)
        def wrapper(*args, **kwargs):
            try:
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
            except:
                return "Invalid Token", 400
        return wrapper
    return decorator

def authenticate_doctor():
    def decorator(funct):
        @functools.wraps(funct)
        def wrapper(*args, **kwargs):
            try:
                token = request.headers.get(jwtConfig.jwt_header_key) 
                decoded_jwt = jwt.decode(token, os.environ.get("JWT_SECRET"),
                    algorithms=[jwtConfig.jwt_algorithm]) 
                doctorUserAuthToken = DoctorUserAuthToken(decoded_jwt)
                print(doctorUserAuthToken)
                if doctorUserAuthToken.type != tokensConfig.doctor_auth_token:
                    return "Invalid Token", 400
                if int(doctorUserAuthToken.expiry) < int(time.time()): 
                    return "Expired Token", 400
                return funct(doctorUserAuthToken.user_id, doctorUserAuthToken.surgery_id, doctorUserAuthToken.doctor_id, *args, **kwargs)
            except:
                return "Invalid Token", 400
        return wrapper
    return decorator