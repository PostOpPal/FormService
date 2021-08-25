from services.mappers.form_entry_request_to_mongo_entry_mapper import form_entry_request_to_mongo_entry
from services.mappers.daily_questionnaire_response_mapper import mongo_surgery_to_daily_questionnaire_response
from services.mappers.entry_mapper import mongo_entry_to_entry_response
from services.mappers.entries_response_mapper import mongo_surgery_to_entries_response
from models.generated_models.requests.form_entry_request import FormEntryRequest
from models.generated_models.responses.success import Success
from mongo_models.user_model import Entry, User, Surgery

def get_daily_questionnaire(user_id: str, surgery_id: str):
    '''Find the current daily questionare for a given user and surgery'''
    user : User = User.objects(oid = user_id).first()
    if user is None: return "User not found", 400
    surgery : Surgery = user.surgeries.get(oid = surgery_id)
    if surgery is None: return "Surgery not found", 400
    return mongo_surgery_to_daily_questionnaire_response(surgery), 200

def get_form_entry_with_id(user_id: str, surgery_id: str, oid: str):
    '''Find a entry given a date, user and surgery'''
    user : User = User.objects(oid = user_id).first()
    if user is None: return "User not found", 400
    surgery : Surgery = user.surgeries.get(oid = surgery_id)
    if surgery is None: return "Surgery not found", 400
    print(oid)
    entry = surgery.entries.get(oid = oid)
    if entry is None: return "Entry not found", 400
    return mongo_entry_to_entry_response(entry, surgery), 200
    
    
def get_submitted_entries(user_id: str, surgery_id: str):
    '''Find the list of dates a user has submitted entries for a given surgery'''
    user : User = User.objects(oid = user_id).first()
    if user is None: return "User not found", 400
    surgery : Surgery = user.surgeries.get(oid = surgery_id)
    if surgery is None: return "Surgery not found", 400
    return mongo_surgery_to_entries_response(surgery), 200

def submit_form_entry(user_id: str, surgery_id: str, form_entry: FormEntryRequest):
    '''Submit a form entry for a given user and surgery'''
    # TODO add support for creating new user if none existant
    success : Success = Success()
    user : User = User.objects(oid = user_id).first()
    if user is None: return "User not found", 400
    surgery : Surgery = user.surgeries.get(oid = surgery_id)
    if surgery is None: return "Surgery not found", 400
    entry : Entry = form_entry_request_to_mongo_entry(form_entry, surgery)
    surgery.entries.append(entry)
    user.save()
    success.success = True
    success.message = "Submitted form entry"
    return success, 200