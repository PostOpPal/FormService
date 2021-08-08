from models.generated_models.requests.form_entry_request import FormEntryRequest
from app import app
from flask_tools.serialise import *
from routes.tools.authenticate import authenticate
from services.user_form_manager import UserFormManager
from models.generated_models.args.form_entry_args_schema import FormEntryArgs

@app.route('/user_questionnaire', methods = ['GET'])
@authenticate()
@serialise()
def get_user_questionnaire(user_id: int, surgery_id: int):
    '''Returns the daily questionnaire for a given user'''
    response, code = UserFormManager.get_daily_questionnaire(user_id, surgery_id)
    return response, code

@app.route('/form_entry', methods = ['GET'])
@deserialise_args(FormEntryArgs)
@serialise()
@authenticate()
def get_form_entry(user_id: int, surgery_id: int, args: FormEntryArgs):
    '''Returns a form entry for a given date for a user'''
    response, code = UserFormManager.get_form_entry_with_date(user_id, surgery_id, args.date)
    return response, code

@app.route('/submitted_dates', methods = ['GET'])
@authenticate()
@serialise()
def get_submitted_dates(user_id: int, surgery_id: int):
    '''Returns a list of dates on which the user has submitted a form'''
    # TODO add pagination
    response, code = UserFormManager.get_submitted_dates(user_id,surgery_id)
    return response, code

@app.route('/form_entry', methods = ['POST'])
@deserialise(FormEntryRequest)
@serialise()
@authenticate()
def post_form_entry(user_id: int, surgery_id: int, form_entry_request : FormEntryRequest):
    print(user_id)
    print(surgery_id)
    print(form_entry_request)
    '''Submits a form entry from the user, sends a request to a queue to recalculate stats for user'''
    response, code = UserFormManager.submit_form_entry(user_id,surgery_id,form_entry_request)
    # TODO Send a message to a queue to recalculate the stats for the user
    return response, code


@app.route('/debug/jwt', methods = ['GET'])
def get_jwt():
    import jwt
    import time
    import os
    from models.generated_models.tokens.user_auth_token import UserAuthToken
    from configs.configs import tokensConfig, jwtConfig
    from mongo_models.user_model import User, Surgery
    userAuthToken = UserAuthToken()
    userAuthToken.expiry = int(time.time()) + 1000000000
    #user : User = User.objects().first()
    userAuthToken.user_id = 1#str(user.oid)
    userAuthToken.surgery_id = 1#str(user.surgeries.first().oid)
    userAuthToken.type = tokensConfig.auth_token
    print(userAuthToken)
    encoded_jwt = jwt.encode(userAuthToken.__dict__, 
        os.environ.get("JWT_SECRET"), algorithm=jwtConfig.jwt_algorithm)
    return encoded_jwt

@app.route('/debug/create_user', methods = ['GET'])
def get_create_user():
    from  mongoengine import connect
    connect(host="mongodb://127.0.0.1:27017/FormService")

    from mongo_models.questionnaire_model import Questionnaire, Question
    question = Question()
    question.question_type = "text"
    question.text = "test normal question"
    questionnaire = Questionnaire()
    print(questionnaire.oid)
    questionnaire.questions.append(question)
    questionnaire.save()

    from mongo_models.user_model import User, Surgery
    surgery = Surgery()
    surgery.oid = 1
    #surgery._id = str(uuid.uuid4)
    surgery.status = 'active'
    surgery.current_doctor_questions.append("test doctor question")
    surgery.questionnaire = questionnaire
    user = User()
    user.oid = 1
    user.surgeries.append(surgery)
    user.save()
    return 'done'