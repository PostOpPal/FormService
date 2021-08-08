from models.generated_models.responses.entry_response import EntryResponse
from mongo_models.user_model import Entry, DoctorResponse, StandardResponse
from mongo_models.questionnaire_model import Question

def mongo_entry_to_entry_response(entry : Entry) -> EntryResponse:
    entryResponse : EntryResponse = EntryResponse()
    entryResponse.date = entry.date
    response : DoctorResponse
    for response in entry.doctor_responses:
        item = EntryResponse.DoctorResponses.Items()
        item.question = response.question
        item.response = response.response
        entryResponse.doctor_responses.append(item)
    response : StandardResponse
    for response in entry.doctor_responses:
        item = EntryResponse.StandardResponses.Items()
        question : Question = response.question
        item.question_type = question.question_type
        item.text = question.text
        if question.scale is not None: item.scale = question.scale
        item.response = response.response
        entryResponse.standard_responses.append(item)

    return entryResponse