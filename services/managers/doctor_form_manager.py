from bson.objectid import ObjectId
from models.generated_models.requests.qb_questions_change_request import QBQuestionChangeRequest
from services.tools.get_user_and_surgery import get_user_and_surgery
from fastapi.exceptions import HTTPException
from mongo_models.questionnaire_model import Questionnaire
from models.generated_models.responses.success import Success
from models.generated_models.requests.doctor_questions_change_request import DoctorQuestionChangeRequest
from models.generated_models.requests.doctor_questionnaire_change_request import DoctorQuestionnaireChangeRequest

def change_user_doctor_questions(user_id : str, surgery_id : str, change_request : DoctorQuestionChangeRequest) -> Success:
    success : Success = Success()
    user, surgery = get_user_and_surgery(user_id, surgery_id)
    surgery.current_doctor_questions = change_request.questions
    user.save()
    success.message = "Changed questions"
    success.success = True
    return success

def change_user_questionnaire(user_id : str, surgery_id : str, change_request : DoctorQuestionnaireChangeRequest) -> Success:
    success : Success = Success()
    user, surgery = get_user_and_surgery(user_id, surgery_id)
    #TODO check this line is valid
    try: questionnaire = Questionnaire.objects(oid = change_request.questionnaire_id).first()
    except: raise HTTPException(status_code = 404, detail = "Questionnaire not found")
    surgery.questionnaire = questionnaire
    user.save()
    success.message = "Changed questionnaire"
    success.success = True
    return success

def change_user_qb_questions(user_id : str, surgery_id : str, change_request : QBQuestionChangeRequest) -> Success:
    success : Success = Success()
    user, surgery = get_user_and_surgery(user_id, surgery_id)
    surgery.qb_questions.clear()
    for question_id in change_request.question_ids:
        surgery.qb_questions.append(ObjectId(question_id))
    success.message = "Changed QB Questions"
    success.success = True
    return success