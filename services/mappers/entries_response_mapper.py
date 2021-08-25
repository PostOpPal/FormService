from models.generated_models.responses.submitted_entries_response import SubmittedEntriesResponse
from mongo_models.user_model import Surgery, Entry

def mongo_surgery_to_entries_response(surgery : Surgery) -> SubmittedEntriesResponse:
    submittedEntriesResponse = SubmittedEntriesResponse()
    entry : Entry 
    submittedEntriesResponse.entries = []
    for entry in surgery.entries:
        _entry : SubmittedEntriesResponse.Entries.Items = SubmittedEntriesResponse.Entries.Items()
        _entry.id = str(entry.oid)
        _entry.date = entry.date
        submittedEntriesResponse.entries.append(_entry)
    return submittedEntriesResponse