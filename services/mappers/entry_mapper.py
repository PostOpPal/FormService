from models.generated_models.responses.entry_response import EntryResponse
from models.generated_models.responses.entry_response import DoctorResponse as ReplyDoctorResponse
from models.generated_models.responses.entry_response import QbResponse as ReplyQbResponse
from models.generated_models.responses.entry_response import StandardResponse as ReplyStandardResponse
from mongo_models.user_model import Entry, DoctorResponse, QBResponse, StandardResponse, Surgery
from mongo_models.questionnaire_model import Question, Questionnaire

def mongo_entry_to_entry_response(entry : Entry, surgery : Surgery) -> EntryResponse:
    entryResponse : EntryResponse = EntryResponse.construct()
    entryResponse.date = entry.date
    entryResponse.id = str(entry.oid)
    response : DoctorResponse
    questionnaire : Questionnaire = surgery.questionnaire
    entryResponse.doctor_responses = []
    for response in entry.doctor_responses:
        item = ReplyDoctorResponse.construct()
        item.question = response.question
        item.response = response.response
        entryResponse.doctor_responses.append(item)
    response : StandardResponse
    entryResponse.standard_responses = []
    for response in entry.standard_responses:
        item = ReplyStandardResponse.construct()
        question : Question =  questionnaire.questions.get(oid = response.question_id)
        item.question_type = question.question_type.value
        item.text = question.text
        if question.scale is not None: item.scale = question.scale
        item.response = response.response
        entryResponse.standard_responses.append(item)
    response : QBResponse
    entryResponse.qb_responses = []
    for response in entry.qb_responses:
        item = ReplyQbResponse.construct()
        question = response.question
        item.qb_question_type = question.question_type.value
        item.text = question.text
        if question.scale is not None: item.scale = question.scale
        item.response = response.response
        entryResponse.qb_responses.append(item)

    return entryResponse