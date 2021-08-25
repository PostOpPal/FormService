from app import app
from flask_tools.serialise import *
from routes.tools.authenticate import authenticate_doctor
import services.user_form_manager as user_form_manager
import services.doctor_form_manager as doctor_form_manager
from models.generated_models.args.form_entry_args_schema import FormEntryArgs
from models.generated_models.requests.doctor_questions_change_request import DoctorQuestionChangeRequest
from models.generated_models.requests.doctor_questionnaire_change_request import DoctorQuestionnaireChangeRequest

@app.route('/doctor/entries', methods = ['GET'])
@authenticate_doctor()
def get_doctor_entries(user_id: str, surgery_id: str, doctor_id: str):
    '''Returns a list of user entry ids and dates'''
    # TODO add pagination
    response, code = user_form_manager.get_submitted_entries(user_id,surgery_id)
    print(response)
    return response, code

@app.route('/doctor/entry', methods = ['GET'])
@deserialise_args(FormEntryArgs)
@authenticate_doctor()
def get_doctor_entry(user_id: str, surgery_id: str, doctor_id: str, args: FormEntryArgs):
    '''Returns the details of a user entry'''
    response, code = user_form_manager.get_form_entry_with_id(user_id, surgery_id, args.id)
    return response, code

@app.route('/doctor/questionnaire', methods = ['GET'])
@authenticate_doctor()
def get_doctor_questionnaire(user_id: str, surgery_id: str, doctor_id: str):
    '''Returns the questionnaire for a given user surgery'''
    response, code = user_form_manager.get_daily_questionnaire(user_id, surgery_id)
    return response, code

@app.route('/doctor/questions', methods = ['POST'])
@deserialise(DoctorQuestionChangeRequest)
@authenticate_doctor()
def post_doctor_questions(user_id: str, surgery_id: str, doctor_id: str, request: DoctorQuestionChangeRequest):
    '''Sets the doctor questions for a user surgery'''
    response, code = doctor_form_manager.change_user_doctor_questions(user_id, surgery_id, request)
    return response, code

#TODO implement questions
@app.route('/doctor/questionnaire', methods = ['POST'])
@deserialise(DoctorQuestionnaireChangeRequest)
@authenticate_doctor()
def post_doctor_questionnaire(user_id: str, surgery_id: str, doctor_id: str, request : DoctorQuestionnaireChangeRequest):
    '''Sets the questionnaire for a user surgery'''
    response, code = doctor_form_manager.change_user_questionnaire(user_id, surgery_id, request)
    return response, code
    return



