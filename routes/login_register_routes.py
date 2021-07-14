from app import app
from flask import request
from routes.tools.serialise import *
from models.generated_models.login_request import *
from models.generated_models.login_response import *
from models.generated_models.register_request import *
from services.user_manager import *


@app.route('/', methods = ['GET'])
def get_root():
    return "api"

@app.route('/login', methods = ['POST'])
@deserialise(Loginrequest)
@serialise()
def login_post(body):
    '''Return a jwt given the users login details if correct'''
    login = body
    loginresponse = Loginresponse()
    valid, jwt = UserManager.generate_jwt(login.email, login.password)
    if valid:
        loginresponse.jwt = jwt
        return loginresponse
    return "Unauthorised", 401

@app.route('/register', methods = ['POST'])
@deserialise(Registerrequest)
def register_post(body):
    #TODO add response json
    '''Register a user'''
    register = body
    valid, message = UserManager.register_user(register.email, register.password, register.code)
    if valid:
        return message
    return message, 400
