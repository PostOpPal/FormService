from mongo_models.user_model import DoctorResponse, Entry, StandardResponse, Surgery
from mongo_models.questionnaire_model import Questionnaire, Question
from models.generated_models.requests.form_entry_request import FormEntryRequest
from datetime import datetime

def form_entry_request_to_mongo_entry(formEntryRequest : FormEntryRequest, surgery : Surgery) -> Entry:
    entry : Entry = Entry()
    entry.date = datetime.today().strftime('%Y-%m-%d')
    questionnaire : Questionnaire = surgery.questionnaire
    response : FormEntryRequest.StandardResponses.Items
    for response in formEntryRequest.standard_responses:
        standardResponse : StandardResponse = StandardResponse()
        standardResponse.question = questionnaire.questions.with_id(response._id)
        standardResponse.response = response.response
        entry.standard_responses.append(standardResponse)
    response : FormEntryRequest.DoctorResponses.Items
    for response in formEntryRequest.doctor_responses:
        doctorResponse : DoctorResponse = DoctorResponse()
        doctorResponse.question = response.question
        doctorResponse.response = response.response
        entry.doctor_responses.append(doctorResponse)
    return entry
