from app import app
from flask import request
from routes.tools.serialise import *

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
