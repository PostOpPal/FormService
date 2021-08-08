from models.generated_models.responses.entry_response import EntryResponse
from mongo_models.user_model import Entry, DoctorResponse, StandardResponse, Surgery
from mongo_models.questionnaire_model import Question, Questionnaire

def mongo_entry_to_entry_response(entry : Entry, surgery : Surgery) -> EntryResponse:
    entryResponse : EntryResponse = EntryResponse()
    entryResponse.date = entry.date
    response : DoctorResponse
    questionnaire : Questionnaire = surgery.questionnaire
    for response in entry.doctor_responses:
        item = EntryResponse.DoctorResponses.Items()
        item.question = response.question
        item.response = response.response
        entryResponse.doctor_responses.append(item)
    response : StandardResponse
    for response in entry.standard_responses:
        item = EntryResponse.StandardResponses.Items()
        question : Question =  questionnaire.questions.get(oid = response.question_id)
        item.question_type = question.question_type.value
        item.text = question.text
        if question.scale is not None: item.scale = question.scale
        item.response = response.response
        entryResponse.standard_responses.append(item)

    return entryResponse