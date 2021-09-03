from bson.objectid import ObjectId
from fastapi.exceptions import HTTPException
from mongo_models.questionnaire_model import Questionnaire
from mongo_models.user_model import DoctorResponse, Entry, QBResponse, StandardResponse, Surgery
from models.generated_models.requests.form_entry_request import StandardResponse as RequestStandardResponse
from models.generated_models.requests.form_entry_request import DoctorResponse as RequestDoctorResponse
from models.generated_models.requests.form_entry_request import FormEntryRequest
from datetime import datetime

def form_entry_request_to_mongo_entry(formEntryRequest : FormEntryRequest, surgery : Surgery) -> Entry:
    entry : Entry = Entry()
    entry.date = datetime.today().strftime('%Y-%m-%d')
    response : FormEntryRequest.StandardResponses.Items
    try: questionnaire = Questionnaire.objects.get(oid = formEntryRequest.questionnaire_id)
    except: raise HTTPException(status_code = 404, detail = "Questionnaire not found")
    response : RequestStandardResponse
    for response in formEntryRequest.standard_responses:
        try : question = questionnaire.questions.get(oid = response.oid)
        except : raise HTTPException(status_code = 404, detail = "question with oid: " + response.oid + " not found")
        standardResponse : StandardResponse = StandardResponse()
        standardResponse.question_id = response.oid
        standardResponse.response = response.response
        entry.standard_responses.append(standardResponse)
    response : RequestDoctorResponse
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
        qb_response.question = ObjectId(response.oid)
        qb_response.response = response.response
        entry.qb_responses.append(qb_response)
    return entry
