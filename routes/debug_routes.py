from mongo_models.questionnaire_model import MongoSymptomQuestionnaire
from typing import List, Optional
from models.generated_models.responses.success import Success
from models.generated_models.responses.submitted_entries_response import SubmittedEntriesResponse
from models.generated_models.responses.entry_response import EntryResponse
from models.generated_models.responses.questionnaire_response import QuestionnaireResponse
from fastapi import Request, Header
from app import app
from routes.tools.authenticate import authenticate
import services.managers.user_form_manager as user_form_manager
from models.generated_models.requests.form_entry_request import FormEntryRequest


@app.get('/debug/jwt', tags=["debug"])
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

@app.get('/debug/create_user', tags=["debug"])
def get_create_user():
    from mongo_models.questionnaire_model import MongoQuestionnaire, MongoQuestion, MongoQBQuestion, MongoSymptomQuestion
    #qb
    qb_question = MongoQBQuestion()
    question = MongoQuestion()
    question.question_type = "text"
    question.question = "test qb question"
    qb_question.question = question
    qb_question.save()
    #questionnaire
    question = MongoQuestion()
    question.question_type = "text"
    question.question = "test normal question"
    questionnaire = MongoQuestionnaire()
    print(questionnaire.oid)
    questionnaire.questions.append(question)
    questionnaire.save()
    #symptom
    symptomTile = MongoSymptomQuestion()
    symptomTile.title = "Symtom tile"
    symptomTile.description = "descroptio"
    question = MongoQuestion()
    question.question_type = "text"
    question.question = "test symptom question"
    symptomTile.follow_up_questions = []
    #symptomTile.follow_up_questions = []
    symptomTile.follow_up_questions.append(question)
    symptomTileQuestionnaire = MongoSymptomQuestionnaire()
    symptomTileQuestionnaire.tiles = []
    symptomTileQuestionnaire.tiles.append(symptomTile)
    symptomTileQuestionnaire.title = "title"
    symptomTileQuestionnaire.save()

    from mongo_models.user_model import MongoUser, MongoSurgery
    surgery = MongoSurgery()
    surgery.oid = 1
    #surgery._id = str(uuid.uuid4)
    surgery.status = 'active'
    surgery.current_doctor_questions.append("test doctor question")
    surgery.questionnaire = questionnaire
    surgery.qb_questions.append(qb_question)
    surgery.symptom_questionnaire = symptomTileQuestionnaire
    surgery.save()
    user = MongoUser()
    user.oid = 1
    user.surgeries.append(surgery)
    user.save()
    return 'done'