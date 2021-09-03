from mongo_models.user_model import DoctorResponse, Entry, QBResponse, StandardResponse, Surgery
from models.generated_models.requests.form_entry_request import FormEntryRequest
from datetime import datetime

def form_entry_request_to_mongo_entry(formEntryRequest : FormEntryRequest, surgery : Surgery) -> Entry:
    entry : Entry = Entry()
    entry.date = datetime.today().strftime('%Y-%m-%d')
    response : FormEntryRequest.StandardResponses.Items
    for response in formEntryRequest.standard_responses:
        standardResponse : StandardResponse = StandardResponse()
        standardResponse.question_id = response.oid
        standardResponse.response = response.response
        entry.standard_responses.append(standardResponse)
    response : FormEntryRequest.DoctorResponses.Items
    for response in formEntryRequest.doctor_responses:
        doctorResponse : DoctorResponse = DoctorResponse()
        doctorResponse.question = response.question
        doctorResponse.response = response.response
        entry.doctor_responses.append(doctorResponse)
    response : FormEntryRequest.QbResponses.Items
    if formEntryRequest.qb_responses is None: formEntryRequest.qb_responses = []
    for response in formEntryRequest.qb_responses:
        qb_response : QBResponse = QBResponse()
        # TODO find the question
        #qb_response.question = 
        qb_response.response = response.response
        entry.qb_responses.append(qb_response)
    return entry
