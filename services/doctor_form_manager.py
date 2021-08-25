from bson.objectid import ObjectId
from mongo_models.questionnaire_model import Question, Questionnaire
from mongo_models.user_model import Surgery, User
from models.generated_models.responses.success import Success
from models.generated_models.requests.doctor_questions_change_request import DoctorQuestionChangeRequest
from models.generated_models.requests.doctor_questionnaire_change_request import DoctorQuestionnaireChangeRequest

def change_user_doctor_questions(user_id : str, surgery_id : str, change_request : DoctorQuestionChangeRequest):
    success : Success = Success()
    user : User = User.objects(oid = user_id).first()
    if user is None: return "User not found", 400
    surgery : Surgery = user.surgeries.get(oid = surgery_id)
    if surgery is None: return "Surgery not found", 400
    surgery.current_doctor_questions = change_request.questions
    user.save()
    success.message = "Changed questions"
    success.success = True
    return success , 200

def change_user_questionnaire(user_id : str, surgery_id : str, change_request : DoctorQuestionnaireChangeRequest):
    success : Success = Success()
    user : User = User.objects(oid = user_id).first()
    if user is None: return "User not found", 400
    surgery : Surgery = user.surgeries.get(oid = surgery_id)
    if surgery is None: return "Surgery not found", 400
    #TODO check this line is valid
    questionnaire = Questionnaire.objects(oid = change_request.questionnaire_id).first()
    if questionnaire is None: return "Questionnaire not found", 400
    surgery.questionnaire = questionnaire
    user.save()
    success.message = "Changed questionnaire"
    success.success = True
    return success , 200