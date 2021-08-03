from app import app
from flask import request
from routes.tools.serialise import *
from routes.tools.authenticate import authenticate
from services.user_form_manager import UserFormManager

@app.route('/user_questionnaire', methods = ['GET'])
@authenticate()
@serialise()
def get_user_questionnaire(user_id: str, surgery_id: str):
    '''Returns the daily questionnaire for a given user'''
    code, response = UserFormManager.get_daily_questionnaire(user_id, surgery_id)
    return response, code

@app.route('/form_entry', methods = ['GET'])
@authenticate()
@serialise()
def get_form_entry(user_id: str, surgery_id: str):
    '''Returns a form entry for a given date for a user'''
    date = request.args.get('date')
    code, response = UserFormManager.get_form_entry_with_date(user_id, surgery_id, date)
    return response, code

@app.route('/submitted_dates', methods = ['GET'])
@authenticate()
@serialise()
def get_submitted_dates(user_id: str, surgery_id: str):
    '''Returns a list of dates on which the user has submitted a form'''
    # TODO add pagination
    code, response = UserFormManager.get_submitted_dates(user_id,surgery_id)
    return response, code

@app.route('/form_entry', methods = ['POST'])
@authenticate()
@serialise()
def get_form_entry(user_id: str, surgery_id: str, form_entry):
    '''Submits a form entry from the user, sends a request to a queue to recalculate stats for user'''
    code, response = UserFormManager.submit_form_entry(user_id,surgery_id,form_entry)
    # TODO Send a message to a queue to recalculate the stats for the user
    return response, code
