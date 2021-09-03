from models.generated_models.responses.questionnaire_response import QuestionnaireResponse
from mongo_models.user_model import Surgery
from mongo_models.questionnaire_model import Questionnaire, Question
from mongo_models.question_bank import QB_Question

def mongo_surgery_to_daily_questionnaire_response(surgery : Surgery) -> QuestionnaireResponse:
    questionnaireResponse = QuestionnaireResponse()
    questionnaire : Questionnaire = surgery.questionnaire
    questionnaireResponse.questionnaire_id = str(questionnaire.oid)
    questionnaireResponse.doctor_questions = []
    for question in surgery.current_doctor_questions:
        questionnaireResponse.doctor_questions.append(question)
    question : Question
    questionnaireResponse.questions = QuestionnaireResponse.Questions()
    for question in questionnaire.questions:
        item = QuestionnaireResponse.QuestionaireQuestions.Items()
        item.question_type = str(question.question_type.value)
        item.text = question.text
        item.scale = question.scale
        item.oid = str(question.oid)
        questionnaireResponse.questionaire_questions.append(item)
    qb_question : QB_Question
    for qb_question in surgery.qb_questions:
        item = QuestionnaireResponse.QbQuestions.Items()
        item.oid = qb_question.oid
        item.question_type = qb_question.question_type
        item.scale = qb_question.scale
        item.text = qb_question.text
        questionnaireResponse.qb_questions.append(item)
    return questionnaireResponse