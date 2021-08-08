from models.generated_models.responses.submitted_dates_response import SubmittedDatesResponse
from mongo_models.user_model import Surgery, Entry

def mongo_surgery_to_dates_response(surgery : Surgery) -> SubmittedDatesResponse:
    submittedDatesResponse = SubmittedDatesResponse()
    entry : Entry 
    for entry in surgery.entries:
        submittedDatesResponse.dates.append(entry.date)
    return submittedDatesResponse