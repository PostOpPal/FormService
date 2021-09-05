from models.generated_models.responses.submitted_entries_response import SubmittedEntriesResponse
from models.generated_models.responses.submitted_entries_response import Entry
from mongo_models.user_model import MongoSurgery, MongoEntry

def mongo_surgery_to_entries_response(surgery : MongoSurgery) -> SubmittedEntriesResponse:
    submittedEntriesResponse = SubmittedEntriesResponse()
    mongo_entry : MongoEntry 
    submittedEntriesResponse.entries = []
    for mongo_entry in surgery.entries:
        entry = Entry.construct()
        entry.id = str(mongo_entry.oid)
        entry.date = mongo_entry.date
        submittedEntriesResponse.entries.append(entry)
    return submittedEntriesResponse