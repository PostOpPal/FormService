from mongo_models.questionnaire_model import MongoQuestionType
from mongo_models.user_model import MongoDoctorResponse, MongoEntry, MongoResponse, MongoSurgery, MongoSymptomResponse
from models.generated_models.requests.form_entry_request import DoctorResponse, FormEntryRequest, StandardResponse, SymptomResponse
from datetime import datetime


def standard_response_to_mongo_response(standard_response : StandardResponse) -> MongoResponse:
    mongo_response = MongoResponse()
    mongo_response.question = standard_response.question
    mongo_response.question_type = MongoQuestionType(standard_response.question_type.value)
    mongo_response.scale = standard_response.scale
    mongo_response.response = standard_response.response
    if mongo_response.follow_up_responses is not None:
        mongo_response.follow_up_responses = [
            standard_response_to_mongo_response(response)
            for response in standard_response.follow_up_responses]
    return mongo_response

def request_doctor_response_to_mongo_doctor_response(doctor_response : DoctorResponse) -> MongoDoctorResponse:
    mongo_doctor_response = MongoDoctorResponse()
    mongo_doctor_response.response = doctor_response.response
    mongo_doctor_response.question = doctor_response.question
    return mongo_doctor_response

def request_symptom_response_to_mongo_symptom_response(symptom_response : SymptomResponse) -> MongoSymptomResponse:
    mongo_symptom_response = MongoSymptomResponse()
    mongo_symptom_response.title = symptom_response.title
    mongo_symptom_response.description = symptom_response.description
    if mongo_symptom_response.follow_up_responses is not None:
        mongo_symptom_response.follow_up_responses = [standard_response_to_mongo_response(response)
            for response in symptom_response.follow_up_responses]
    return mongo_symptom_response

def form_entry_request_to_mongo_entry(form_entry_request : FormEntryRequest, surgery : MongoSurgery) -> MongoEntry:
    mongo_entry = MongoEntry()
    mongo_entry.date = datetime.today().strftime('%Y-%m-%d')
    mongo_entry.questionnaire_id = form_entry_request.standard_questionnaire_id
    mongo_entry.symptom_questionnaire_id = form_entry_request.symptom_questionnaire_id
    # doctor questionnaire
    mongo_entry.doctor_responses = [request_doctor_response_to_mongo_doctor_response(doctor_response)
        for doctor_response in form_entry_request.doctor_responses]
    # standard questionnaire
    mongo_entry.standard_responses = [standard_response_to_mongo_response(standard_response)
        for standard_response in form_entry_request.standard_responses]
    # qb questions
    mongo_entry.qb_responses = [standard_response_to_mongo_response(standard_response)
        for standard_response in form_entry_request.qb_responses]
    # symptom tile questions
    mongo_entry.symptom_responses = [request_symptom_response_to_mongo_symptom_response(symptom_response)
        for symptom_response in form_entry_request.symptom_responses]
    return mongo_entry
