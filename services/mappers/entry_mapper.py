from typing import List
from models.generated_models.responses.entry_response import EntryResponse
from models.generated_models.responses.entry_response import DoctorResponse as ReplyDoctorResponse
from models.generated_models.responses.entry_response import Response as ReplyResponse
from mongo_models.user_model import Entry, DoctorResponse, Response, Surgery
from mongo_models.questionnaire_model import Question, Questionnaire

def create_response_list(responses : List[Response]) -> List[ReplyResponse]:
    '''Maps a list of mongo responses to a list of questionnaire responses'''
    if responses is None or responses == []: return []
    result = []
    for response in responses:
        replyResponse = ReplyResponse.construct()
        replyResponse.question = response.question
        replyResponse.response = response.response
        replyResponse.question_type = response.question_type
        replyResponse.follow_up_entries = create_response_list(response.follow_up_responses)
        result.append(replyResponse)
    return result

def mongo_response_to_reply_response(response : Response) -> ReplyResponse:
    item = ReplyResponse.construct()
    item.question_type = response.question_type.value
    item.text = response.question
    if response.scale is not None: item.scale = response.scale
    item.response = response.response
    item.follow_up_entries = create_response_list(response.follow_up_responses)
    return item

def mongo_doctor_response_to_reply_doctor_response(response : DoctorResponse) -> ReplyDoctorResponse:
    item = ReplyDoctorResponse.construct()
    item.question = response.question
    item.response = response.response
    return item

def mongo_entry_to_entry_response(entry : Entry, surgery : Surgery) -> EntryResponse:
    entryResponse : EntryResponse = EntryResponse.construct()
    entryResponse.date = entry.date
    entryResponse.id = str(entry.oid)
    # doctor responses
    entryResponse.doctor_responses = [mongo_doctor_response_to_reply_doctor_response(response)
        for response in entry.doctor_responses]
    # standard responses
    entryResponse.standard_responses = [mongo_response_to_reply_response(response)
        for response in entry.standard_responses]
    # entry responses
    entryResponse.qb_responses = [mongo_response_to_reply_response(response)
        for response in entry.qb_responses]
    return entryResponse