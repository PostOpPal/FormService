from component_test.conftest import *
import hashlib
from app import db
from configs.configs import *
from sqlalchemy_models.models import *
import os
import json
import os
import jwt
import time

mimetype = 'application/json'
headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}

def test_empty_db_default_root(client):
    """Start with a blank database."""
    print()
    print("-----------------------------")
    print("Running test_empty_db_default_root")
    rv = client.get('/')
    assert b'api' in rv.data
    print("-----------------------------")

def test_login_correct(client):
    """Start with a blank database."""
    print()
    print("-----------------------------")
    print("Running test_login_correct")

    password = "test"
    salt = os.urandom(64)
    password_hash = hashlib.pbkdf2_hmac(hashConfig.password_hash_algorithm, password.encode('utf-8'), salt, hashConfig.hash_repetitions)
    email = "test@test.com"
    code = os.urandom(64)
    user = User(password_hash = password_hash, salt = salt, email = email, code = code)
    db.session.add(user)
    db.session.commit()

    data = {
        "email":email,
        "password":password
    }
    response = client.post("/login", data=json.dumps(data), headers=headers)
    data = json.loads(response.data.decode("utf-8") )
    token = jwt.decode(data["jwt"], os.environ.get("JWT_SECRET"), algorithms=[jwtConfig.jwt_algorithm])
    assert email == token["email"]
    assert ((token["expiry"] > int(time.time()) )and (token["expiry"] <= int(time.time()) + jwtConfig.jwt_expiry))
    #assert b'api' in response.data
    print("-----------------------------")