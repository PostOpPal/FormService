from models.generated_models.responses.questionnaire_response import QuestionnaireResponse
from mongo_models.user_model import Surgery
from mongo_models.questionnaire_model import Questionnaire, Question

def mongo_surgery_to_daily_questionnaire_response(surgery : Surgery) -> QuestionnaireResponse:
    questionnaireResponse = QuestionnaireResponse()
    questionnaire : Questionnaire = surgery.questionnaire
    questionnaireResponse.questionnaire_id = questionnaire._id
    for question in surgery.current_doctor_questions:
        questionnaireResponse.doctor_questions.append(question)
    question : Question
    for question in questionnaire.questions:
        item = QuestionnaireResponse.Questions.Items()
        item.question_type = question.question_type
        item.text = question.text
        item.scale = question.scale
        item._id = question._id
        questionnaireResponse.questions.append(item)
    return questionnaireResponse