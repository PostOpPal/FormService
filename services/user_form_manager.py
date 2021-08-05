from mongo_models.generated_models.user_structure_schema import Userstructure
from mongo_models.generated_models.questionaire_structure_schema import Standardquestionnaire

class UserFormManager:

    # TODO need to be able to get the current set of questions for the day
    @staticmethod
    def get_daily_questionnaire(user_id: str, surgery_id: str):
        '''Find the current daily questionare for a given user'''
        # request the user structure from mongo db
        # request the questionnaire from mongo db
        # combine the questionnaire and the doctor questions into one response object
        # return the response object
        return "Unimplemented", 400

    # TODO need to be able to get a form from the past given id or given date
    @staticmethod
    def get_form_entry_with_date(user_id: str, surgery_id: str, date: str):
        return "Unimplemented", 400
        
    # TODO need to be able to get a list of dates on which a form was submitted
    @staticmethod
    def get_submitted_dates(user_id: str, surgery_id: str):
        return "Unimplemented", 400

    # TODO need to be able to submit a new form entry, should return a score for the entry
    @staticmethod
    def submit_form_entry(user_id: str, surgery_id: str, form_entry):
        return "Unimplemented", 400