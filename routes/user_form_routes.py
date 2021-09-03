from models.generated_models.responses.success import Success
from models.generated_models.responses.submitted_entries_response import SubmittedEntriesResponse
from models.generated_models.responses.entry_response import EntryResponse
from models.generated_models.responses.questionnaire_response import QuestionnaireResponse
from fastapi import Request
from app import app
from routes.tools.authenticate import authenticate
import services.managers.user_form_manager as user_form_manager
from models.generated_models.requests.form_entry_request import FormEntryRequest
from  mongoengine import connect
connect(host="mongodb://localhost:27017/FormService")

@app.get('/user_questionnaire', response_model = QuestionnaireResponse, responses={404: {"model": str}})
@authenticate()
def get_user_questionnaire(request : Request) -> QuestionnaireResponse:
    '''Returns the daily questionnaire for a given user'''
    reply : QuestionnaireResponse 
    reply = user_form_manager.get_daily_questionnaire(request.user_id, request.surgery_id)
    return reply

@app.get('/form_entry', response_model = EntryResponse, responses={404: {"model": str}})
@authenticate()
def get_form_entry(request : Request, id: str) -> EntryResponse:
    '''Returns a form entry for a given date for a user'''
    reply = user_form_manager.get_form_entry_with_id(request.user_id, request.surgery_id, id)
    return reply

@app.get('/submitted_entries', response_model = SubmittedEntriesResponse, responses={404: {"model": str}})
@authenticate()
def get_submitted_entries(request : Request) -> SubmittedEntriesResponse:
    '''Returns a list of dates on which the user has submitted a form'''
    #TODO add pagination
    reply = user_form_manager.get_submitted_entries(request.user_id,request.surgery_id)
    return reply

@app.post('/form_entry', response_model = Success, responses={404: {"model": str}})
#@deserialise(FormEntryRequest)
@authenticate()
def post_form_entry(request : Request, form_entry_request : FormEntryRequest) -> Success:
    '''Submits a form entry from the user, sends a request to a queue to recalculate stats for user'''
    reply = user_form_manager.submit_form_entry(request.user_id, request.surgery_id, form_entry_request)
    # TODO Send a message to a queue to recalculate the stats for the user
    return reply


@app.get('/debug/jwt')
def get_jwt():
    import jwt
    import time
    import os
    from models.generated_models.tokens.user_auth_token import UserAuthToken
    from configs.configs import tokensConfig, jwtConfig
    from mongo_models.user_model import User, Surgery
    userAuthToken = UserAuthToken.construct()
    userAuthToken.expiry = int(time.time()) + 1000000000
    #user : User = User.objects().first()
    userAuthToken.user_id = 1#str(user.oid)
    userAuthToken.surgery_id = 1#str(user.surgeries.first().oid)
    userAuthToken.type = tokensConfig.auth_token
    print(userAuthToken)
    encoded_jwt = jwt.encode(userAuthToken.__dict__, 
        os.environ.get("JWT_SECRET"), algorithm=jwtConfig.jwt_algorithm)
    return encoded_jwt

@app.get('/debug/create_user')
def get_create_user():
    from mongo_models.questionnaire_model import Questionnaire, Question
    question = Question()
    question.question_type = "text"
    question.text = "test normal question"
    questionnaire = Questionnaire()
    print(questionnaire.oid)
    questionnaire.questions.append(question)
    questionnaire.save()
    print("hello")
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