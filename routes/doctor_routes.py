from models.generated_models.requests.qb_questions_change_request import QBQuestionChangeRequest
from models.generated_models.responses.success import Success
from models.generated_models.responses.questionnaire_response import QuestionnaireResponse
from models.generated_models.responses.entry_response import EntryResponse
from models.generated_models.responses.submitted_entries_response import SubmittedEntriesResponse
from fastapi import Request
from app import app
from routes.tools.authenticate import authenticate_doctor
import services.managers.user_form_manager as user_form_manager
import services.managers.doctor_form_manager as doctor_form_manager
from models.generated_models.requests.doctor_questions_change_request import DoctorQuestionChangeRequest
from models.generated_models.requests.doctor_questionnaire_change_request import DoctorQuestionnaireChangeRequest

@app.get('/doctor/entries', response_model = SubmittedEntriesResponse, responses={404: {"model": str}}, tags=["doctor"])
@authenticate_doctor()
def get_doctor_entries(request : Request) -> SubmittedEntriesResponse:
    '''Returns a list of user entry ids and dates'''
    response = user_form_manager.get_submitted_entries(request.user_id,request.surgery_id)
    return response

@app.get('/doctor/entry', response_model = EntryResponse, responses={404: {"model": str}}, tags=["doctor"])
@authenticate_doctor()
def get_doctor_entry(request : Request, id : str) -> EntryResponse:
    '''Returns the details of a user entry'''
    response = user_form_manager.get_form_entry_with_id(request.user_id, request.surgery_id, id)
    return response

@app.get('/doctor/questionnaire', response_model = QuestionnaireResponse, responses={404: {"model": str}}, tags=["doctor"])
@authenticate_doctor()
def get_doctor_questionnaire(request : Request) -> QuestionnaireResponse:
    '''Returns the questionnaire for a given user surgery'''
    response = user_form_manager.get_daily_questionnaire(request.user_id, request.surgery_id)
    return response

@app.post('/doctor/docotor_questions', response_model = Success, responses={404: {"model": str}}, tags=["doctor"])
@authenticate_doctor()
def post_doctor_questions(request : Request, change_request: DoctorQuestionChangeRequest) -> Success:
    '''Sets the doctor questions for a user surgery'''
    response = doctor_form_manager.change_user_doctor_questions(request.user_id, request.surgery_id, change_request)
    return response

@app.post('/doctor/questionnaire', response_model = Success, responses={404: {"model": str}}, tags=["doctor"])
@authenticate_doctor()
def post_doctor_questionnaire(request : Request, change_request : DoctorQuestionnaireChangeRequest) -> Success:
    '''Sets the questionnaire for a user surgery'''
    response = doctor_form_manager.change_user_questionnaire(request.user_id, request.surgery_id, change_request)
    return response

@app.post("/doctor/qb_questions", response_model = Success, responses={404: {"model": str}}, tags=["doctor"])
@authenticate_doctor()
def post_qb_questions(request : Request, change_request : QBQuestionChangeRequest) -> Success:
    '''Allows the doctor to change the list of question bank questions for the user'''
    response = doctor_form_manager.change_user_qb_questions(request.user_id, request.surgery_id, change_request)
    return response