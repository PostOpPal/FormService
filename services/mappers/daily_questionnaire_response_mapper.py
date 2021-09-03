from models.generated_models.responses.entry_response import QbQuestionType
from models.generated_models.responses.questionnaire_response import QbQuestion, QuestionaireQuestion, QuestionnaireResponse
from mongo_models.user_model import Surgery
from mongo_models.questionnaire_model import Questionnaire, Question
from mongo_models.question_bank import QB_Question

def mongo_surgery_to_daily_questionnaire_response(surgery : Surgery) -> QuestionnaireResponse:
    questionnaireResponse = QuestionnaireResponse.construct()
    questionnaire : Questionnaire = surgery.questionnaire
    questionnaireResponse.questionnaire_id = str(questionnaire.oid)
    questionnaireResponse.doctor_questions = []
    for question in surgery.current_doctor_questions:
        questionnaireResponse.doctor_questions.append(question)
    question : Question
    questionnaireResponse.questionaire_questions = []
    for question in questionnaire.questions:
        item = QuestionaireQuestion.construct()
        item.question_type = str(question.question_type.value)
        item.text = question.text
        item.scale = question.scale
        item.oid = str(question.oid)
        questionnaireResponse.questionaire_questions.append(item)
    qb_question : QB_Question
    questionnaireResponse.qb_questions = []
    for qb_question in surgery.qb_questions:
        item = QbQuestion.construct()
        item.oid = str(qb_question.oid)
        print(qb_question.to_json())
        item.qb_question_type = str(qb_question.question_type.value)
        item.scale = qb_question.scale
        item.text = qb_question.text
        questionnaireResponse.qb_questions.append(item)
        print(item)
    return questionnaireResponse