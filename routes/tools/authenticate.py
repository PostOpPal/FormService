import functools
from fastapi import Request
from fastapi.exceptions import HTTPException
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
                request : Request = kwargs["request"]
                token = bytes(request.headers[jwtConfig.jwt_header_key], 'utf-8')
                decoded_jwt = jwt.decode(token, os.environ.get("JWT_SECRET"),
                    algorithms=[jwtConfig.jwt_algorithm]) 
                userAuthToken = UserAuthToken(**decoded_jwt)
                print(userAuthToken)
                if userAuthToken.type != tokensConfig.auth_token:
                    raise HTTPException(status_code = 400, detail = "Invalid Token")
                if int(userAuthToken.expiry) < int(time.time()): 
                    raise HTTPException(status_code = 400, detail = "Expired Token")
                request.user_id = userAuthToken.user_id
                request.surgery_id = userAuthToken.surgery_id
                return funct(*args, **kwargs)
            except:
                raise HTTPException(status_code = 400, detail = "Token missing")
        return wrapper
    return decorator

# def authenticate_doctor():
#     def decorator(funct):
#         @functools.wraps(funct)
#         def wrapper(*args, **kwargs):
#             try:
#                 token = request.headers.get(jwtConfig.jwt_header_key) 
#                 decoded_jwt = jwt.decode(token, os.environ.get("JWT_SECRET"),
#                     algorithms=[jwtConfig.jwt_algorithm]) 
#                 doctorUserAuthToken = DoctorUserAuthToken(decoded_jwt)
#                 print(doctorUserAuthToken)
#                 if doctorUserAuthToken.type != tokensConfig.doctor_auth_token:
#                     return "Invalid Token", 400
#                 if int(doctorUserAuthToken.expiry) < int(time.time()): 
#                     return "Expired Token", 400
#                 return funct(doctorUserAuthToken.user_id, doctorUserAuthToken.surgery_id, doctorUserAuthToken.doctor_id, *args, **kwargs)
#             except:
#                 return "Invalid Token", 400
#         return wrapper
#     return decorator