from typing import List
from models.generated_models.responses.questionnaire_response import QuestionnaireResponse
from models.generated_models.responses.questionnaire_response import Question as ResponseQuestion
from models.generated_models.responses.questionnaire_response import SymptomTile as ResponseSymptomTile
from mongo_models.user_model import Surgery
from mongo_models.questionnaire_model import Questionnaire, Question, SymptomTile, SymptomTileQuestionnaire
from mongo_models.question_bank import QB_Question

def create_question_list(questions : List[Question]) -> List[ResponseQuestion]:
    '''Maps a list of mongo questions to a list of questionnaire response questions'''
    if questions is None or questions == []: return []
    for question in questions:
        responseQuestion = ResponseQuestion.construct()
        responseQuestion.text = question.text
        responseQuestion.qb_question_type = question.question_type
        responseQuestion.scale = question.scale
        responseQuestion.options = question.options
        for follow_up_questions in responseQuestion.follow_up_questions:
            response_follow_up_questions = create_question_list(follow_up_questions)
            responseQuestion.follow_up_questions.append(response_follow_up_questions)

def mongo_question_to_response_question(question : Question) -> ResponseQuestion:
    item = ResponseQuestion.construct()
    item.question_type = str(question.question_type.value)
    item.text = question.text
    item.scale = question.scale
    item.oid = str(question.oid)
    for questions in question.follow_up_questions:
        response_questions = [mongo_question_to_response_question(question) for question in questions]
        item.follow_up_questions.append(response_questions)


def mongo_surgery_to_daily_questionnaire_response(surgery : Surgery) -> QuestionnaireResponse:
    questionnaireResponse = QuestionnaireResponse.construct()
    questionnaire : Questionnaire = surgery.questionnaire
    symptom_tile_questionnaire : SymptomTileQuestionnaire = surgery.symptom_tile_questionnaire
    questionnaireResponse.questionnaire_id = str(questionnaire.oid)
    # doctor questions
    questionnaireResponse.doctor_questions = surgery.current_doctor_questions
    # standard questions
    question : Question
    questionnaireResponse.questionaire_questions = [mongo_question_to_response_question(question)
        for question in questionnaire.questions]
    for question in questionnaire.questions:
        item = ResponseQuestion.construct()
        item.question_type = str(question.question_type.value)
        item.text = question.text
        item.scale = question.scale
        item.oid = str(question.oid)
        for questions in question.follow_up_questions:
            item.follow_up_questions.append(create_question_list(questions))
        questionnaireResponse.questionaire_questions.append(item)
    qb_question : QB_Question
    questionnaireResponse.qb_questions = []
    for qb_question in surgery.qb_questions:
        qb_question = qb_question.question
        item = ResponseQuestion.construct()
        item.oid = str(qb_question.oid)
        print(qb_question.to_json())
        item.qb_question_type = str(qb_question.question_type.value)
        item.scale = qb_question.scale
        item.text = qb_question.text
        for questions in qb_question.follow_up_questions:
            item.follow_up_questions.append(create_question_list(questions))
        questionnaireResponse.qb_questions.append(item)
    tile : SymptomTile
    for tile in symptom_tile_questionnaire.tiles:
        symptom_tile = ResponseSymptomTile.construct()
        symptom_tile.title = tile.title
        symptom_tile.description = tile.description
        for questions in tile.follow_up_questions:
            symptom_tile.follow_up_questions.append(create_question_list(questions))
        questionnaireResponse.symptom_tiles.append(symptom_tile)
    return questionnaireResponse