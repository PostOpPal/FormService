from app import app
from flask import request
from flask_tools.serialise import *
from routes.tools.authenticate import authenticate
from services.user_form_manager import UserFormManager
from models.generated_models.form_entry_args_schema import FormEntryArgs

@app.route('/user_questionnaire', methods = ['GET'])
@authenticate()
@serialise()
def get_user_questionnaire(user_id: str, surgery_id: str):
    '''Returns the daily questionnaire for a given user'''
    response, code = UserFormManager.get_daily_questionnaire(user_id, surgery_id)
    return response, code

# TODO check authenticate is in correct order
@app.route('/form_entry', methods = ['GET'])
@authenticate()
@deserialise_args(FormEntryArgs)
@serialise()
def get_form_entry(user_id: str, surgery_id: str, args: FormEntryArgs):
    '''Returns a form entry for a given date for a user'''
    response, code = UserFormManager.get_form_entry_with_date(user_id, surgery_id, args.date)
    return response, code

@app.route('/submitted_dates', methods = ['GET'])
@authenticate()
@serialise()
def get_submitted_dates(user_id: str, surgery_id: str):
    '''Returns a list of dates on which the user has submitted a form'''
    # TODO add pagination
    response, code = UserFormManager.get_submitted_dates(user_id,surgery_id)
    return response, code

@app.route('/form_entry', methods = ['POST'])
@authenticate()
@serialise()
def get_form_entry(user_id: str, surgery_id: str, form_entry):
    '''Submits a form entry from the user, sends a request to a queue to recalculate stats for user'''
    response, code = UserFormManager.submit_form_entry(user_id,surgery_id,form_entry)
    # TODO Send a message to a queue to recalculate the stats for the user
    return response, code
