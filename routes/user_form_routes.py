from models.generated_models.responses.success import Success
from models.generated_models.responses.submitted_entries_response import SubmittedEntriesResponse
from models.generated_models.responses.entry_response import EntryResponse
from models.generated_models.responses.questionnaire_response import QuestionnaireResponse
from fastapi import Request
from app import app
from routes.tools.authenticate import authenticate
import services.managers.user_form_manager as user_form_manager
from models.generated_models.requests.form_entry_request import FormEntryRequest

@app.get('/user/user_questionnaire', response_model = QuestionnaireResponse, responses={404: {"model": str}}, tags=["user"])
@authenticate()
def get_user_questionnaire(request : Request) -> QuestionnaireResponse:
    '''Returns the daily questionnaire for a given user'''
    reply : QuestionnaireResponse 
    reply = user_form_manager.get_daily_questionnaire(request.user_id, request.surgery_id)
    print(reply)
    return reply

@app.get('/user/form_entry', response_model = EntryResponse, responses={404: {"model": str}}, tags=["user"])
@authenticate()
def get_form_entry(request : Request, id: str) -> EntryResponse:
    '''Returns a form entry for a given date for a user'''
    reply = user_form_manager.get_form_entry_with_id(request.user_id, request.surgery_id, id)
    return reply

@app.get('/user/submitted_entries', response_model = SubmittedEntriesResponse, responses={404: {"model": str}}, tags=["user"])
@authenticate()
def get_submitted_entries(request : Request) -> SubmittedEntriesResponse:
    '''Returns a list of dates on which the user has submitted a form'''
    #TODO add pagination
    reply = user_form_manager.get_submitted_entries(request.user_id,request.surgery_id)
    return reply

@app.post('/user/form_entry', response_model = Success, responses={404: {"model": str}}, tags=["user"])
#@deserialise(FormEntryRequest)
@authenticate()
def post_form_entry(request : Request, form_entry_request : FormEntryRequest) -> Success:
    '''Submits a form entry from the user, sends a request to a queue to recalculate stats for user'''
    reply = user_form_manager.submit_form_entry(request.user_id, request.surgery_id, form_entry_request)
    # TODO Send a message to a queue to recalculate the stats for the user
    return reply