import hashlib
from app import db
from configs.configs import *
from sqlalchemy_models.models import *
import os
import jwt
import time

class UserManager:

    @staticmethod
    def register_user(email: str, password: str, code: str):
        #TODO check that user doesn't exist yet
        user = User.query.filter_by(email=email).first()
        if user is not None:
            return False,"Username Taken"
        #TODO add logic to connect code with doctor
        salt = os.urandom(64)
        #uses 100000 iterations
        key = hashlib.pbkdf2_hmac(hashConfig.password_hash_algorithm, password.encode('utf-8'), salt, hashConfig.hash_repetitions)
        user = User(email = email, password_hash = key, salt = salt, code = code)
        db.session.add(user)
        db.session.commit()
        return True, "Created User"


    @staticmethod
    def generate_jwt(email: str, password: str):
        user = User.query.filter_by(email=email).first()
        salt = user.salt
        key = hashlib.pbkdf2_hmac(hashConfig.password_hash_algorithm, password.encode('utf-8'), salt, hashConfig.hash_repetitions)
        valid = key == user.password_hash
        if valid == False:
            return False, ""
        #TODO add config for expiry
        expiry = int(time.time()) + jwtConfig.jwt_expiry
        encoded_jwt = jwt.encode({jwtConfig.email_key: email,
            jwtConfig.expiry_key: expiry}, os.environ.get("JWT_SECRET"), algorithm=jwtConfig.jwt_algorithm)
        return True, encoded_jwt

    @staticmethod
    def validate_jwt(encoded_jwt: str, email: str):
        decoded_jwt = jwt.decode(encoded_jwt, os.environ.get("JWT_SECRET"), algorithms=[jwtConfig.jwt_algorithm])
        if decoded_jwt[jwtConfig.email_key] != email: return False, "Invalid username"
        if int(decoded_jwt[jwtConfig.expiry_key]) < int(time,time()): return False, "Expired"
        return True, "Valid"