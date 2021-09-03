from mongo_models.user_model import DoctorResponse, Entry, Response, Surgery, SymptomTileResponse
from models.generated_models.requests.form_entry_request import DoctorEntry, FormEntryRequest, SymptomEntry
from models.generated_models.requests.form_entry_request import StandardEntry
from datetime import datetime


def request_response_to_mongo_response(request_response : StandardEntry) -> Response:
    mongo_response : Response = Response()
    mongo_response.question = request_response.text
    mongo_response.question_type = request_response.question_type
    mongo_response.scale = request_response.scale
    mongo_response.response = request_response.response
    mongo_response.follow_up_responses = [
        request_response_to_mongo_response(request_response)
        for request_response in request_response.follow_up_entries]
    return mongo_response

def request_doctor_response_to_mongo_doctor_response(request_doctor_response : DoctorEntry) -> DoctorResponse:
    doctorResponse = DoctorResponse()
    doctorResponse.response = request_doctor_response.response
    doctorResponse.question = request_doctor_response.question

def request_sysmptom_response_to_mongo_symptom_response(symptom_response : SymptomEntry) -> SymptomTileResponse:
    symptomTileResponse = SymptomTileResponse()
    symptomTileResponse.title = symptom_response.title
    symptomTileResponse.description = symptom_response.description
    symptomTileResponse.follow_up_responses = [request_doctor_response_to_mongo_doctor_response(entry)
        for entry in symptom_response.follow_up_entries]

def form_entry_request_to_mongo_entry(formEntryRequest : FormEntryRequest, surgery : Surgery) -> Entry:
    entry : Entry = Entry()
    entry.date = datetime.today().strftime('%Y-%m-%d')
    # doctor questionnaire
    entry.doctor_responses = [request_doctor_response_to_mongo_doctor_response(doctor_entry)
        for doctor_entry in formEntryRequest.doctor_responses]
    # standard questionnaire
    entry.standard_responses = [request_response_to_mongo_response(standard_response)
        for standard_response in formEntryRequest.standard_responses]
    # qb questions
    entry.qb_responses = [request_response_to_mongo_response(standard_response)
        for standard_response in formEntryRequest.qb_responses]
    # symptom tile questions
    entry.symptom_tile_responses = [request_sysmptom_response_to_mongo_symptom_response(symptom_response)
        for symptom_response in formEntryRequest.symptom_responses]
    return entry
