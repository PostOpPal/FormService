from typing import List
from models.generated_models.responses.questionnaire_response import QuestionnaireResponse
from models.generated_models.responses.questionnaire_response import Question
from models.generated_models.responses.questionnaire_response import SymptomQuestion
from mongo_models.user_model import MongoSurgery
from mongo_models.questionnaire_model import MongoQuestionnaire, MongoSymptomQuestionnaire, MongoSymptomQuestion
from mongo_models.questionnaire_model import MongoQuestion

def mongo_question_to_response_question(mongo_question : MongoQuestion) -> Question:
    response_question = Question.construct()
    response_question.question_type = str(mongo_question.question_type.value)
    response_question.question = mongo_question.question
    response_question.scale = mongo_question.scale
    response_question.oid = str(mongo_question.oid)
    if mongo_question.follow_up_questions is not None:
        for questions in mongo_question.follow_up_questions:
            response_questions = [mongo_question_to_response_question(question) for question in questions]
            response_question.follow_up_questions.append(response_questions)
    return response_question

def mongo_symptom_to_response_symptom(mongo_symptom_question : MongoSymptomQuestion) -> SymptomQuestion:
    response_symptom_question = SymptomQuestion.construct()
    response_symptom_question.oid = str(mongo_symptom_question.oid)
    response_symptom_question.title = mongo_symptom_question.title
    response_symptom_question.description = mongo_symptom_question.description
    if mongo_symptom_question.follow_up_questions is not None:
        response_symptom_question.follow_up_questions = [mongo_question_to_response_question(question)
            for question in mongo_symptom_question.follow_up_questions]
    return response_symptom_question


def mongo_surgery_to_daily_questionnaire_response(surgery : MongoSurgery) -> QuestionnaireResponse:
    questionnaire_response = QuestionnaireResponse.construct()
    mongo_questionnaire : MongoQuestionnaire = surgery.questionnaire
    mongo_symptom_questionnaire : MongoSymptomQuestionnaire = surgery.symptom_questionnaire
    questionnaire_response.standard_questionnaire_id = str(mongo_questionnaire.oid)
    questionnaire_response.symptom_questionnaire_id = str(mongo_symptom_questionnaire.oid)
    # doctor questions
    questionnaire_response.doctor_questions = [doctor_question 
        for doctor_question in surgery.current_doctor_questions]
    # standard questions
    if mongo_questionnaire.questions is not None:
        questionnaire_response.questionaire_questions = [mongo_question_to_response_question(question)
            for question in mongo_questionnaire.questions]
    # question bank questions
    if surgery.qb_questions is not None:
        questionnaire_response.qb_questions = [mongo_question_to_response_question(qb_question.question)
            for qb_question in surgery.qb_questions]
    # symptom questions
    if mongo_symptom_questionnaire is not None:
        questionnaire_response.symptom_questions = [mongo_symptom_to_response_symptom(symptom_questions)
            for symptom_questions in mongo_symptom_questionnaire.questions]
    return questionnaire_response