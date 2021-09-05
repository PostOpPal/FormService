from typing import List
from models.generated_models.responses.entry_response import EntryResponse, QuestionType, SymptomResponse
from models.generated_models.responses.entry_response import DoctorResponse
from models.generated_models.responses.entry_response import Response
from mongo_models.user_model import MongoEntry, MongoDoctorResponse, MongoResponse, MongoSurgery, MongoSymptomResponse

def create_response_list(mongo_responses : List[MongoResponse]) -> List[Response]:
    '''Maps a list of mongo responses to a list of questionnaire responses'''
    if mongo_responses is None or mongo_responses == []: return []
    responses = []
    for mongo_response in mongo_responses:
        response = Response.construct()
        response.question = mongo_response.question
        response.response = mongo_response.response
        response.question_type = QuestionType(mongo_response.question_type.value)
        response.follow_up_responses = create_response_list(mongo_response.follow_up_responses)
        responses.append(response)
    return responses

def mongo_response_to_reply_response(mongo_response : MongoResponse) -> Response:
    response = Response.construct()
    response.question_type = QuestionType(mongo_response.question_type.value)
    response.question = mongo_response.question
    if response.scale is not None: response.scale = mongo_response.scale
    response.response = mongo_response.response
    response.follow_up_responses = create_response_list(mongo_response.follow_up_responses)
    return response

def mongo_doctor_response_to_reply_doctor_response(mongo_doctor_response : MongoDoctorResponse) -> DoctorResponse:
    doctor_response = DoctorResponse.construct()
    doctor_response.question = mongo_doctor_response.question
    doctor_response.response = mongo_doctor_response.response
    return doctor_response

def mongo_symptom_to_response_symptom(mongo_symptom_response : MongoSymptomResponse) -> SymptomResponse:
    symptom_response = SymptomResponse.construct()
    symptom_response.title = mongo_symptom_response.title
    symptom_response.description = mongo_symptom_response.description
    symptom_response.follow_up_responses = create_response_list(mongo_symptom_response.follow_up_responses)
    return symptom_response

def mongo_entry_to_entry_response(entry : MongoEntry, surgery : MongoSurgery) -> EntryResponse:
    entry_response : EntryResponse = EntryResponse.construct()
    entry_response.date = entry.date
    entry_response.id = str(entry.oid)
    # doctor responses
    entry_response.doctor_responses = [mongo_doctor_response_to_reply_doctor_response(response)
        for response in entry.doctor_responses]
    # standard responses
    entry_response.standard_responses = [mongo_response_to_reply_response(response)
        for response in entry.standard_responses]
    # entry responses
    entry_response.qb_responses = [mongo_response_to_reply_response(response)
        for response in entry.qb_responses]
    # symptoms
    entry_response.syptom_responses = [mongo_symptom_to_response_symptom(response)
        for response in entry.symptom_responses]
    return entry_response