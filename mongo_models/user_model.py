from mongo_models.doctor_model import Patient
from mongo_models.question_bank import QB_Question
from mongoengine.document import EmbeddedDocument
from mongo_models.questionnaire_model import Question_Type, Questionnaire, SymptomTileQuestionnaire
from mongoengine import Document
from mongoengine.fields import EmbeddedDocumentListField, EnumField, IntField, ReferenceField
from mongoengine.fields import ListField, StringField, ObjectIdField
from enum import Enum
from bson.objectid import ObjectId

class Status(Enum):
    ACTIVE = 'active'
    COMPLETE = 'complete'

class DoctorResponse(EmbeddedDocument):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    question = StringField()
    response = StringField()

class Response(EmbeddedDocument):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    question = StringField()
    question_type = EnumField(Question_Type, required = True)
    scale = IntField()
    response = StringField()
    follow_up_responses = EmbeddedDocumentListField('Response')

class SymptomTileResponse(EmbeddedDocument):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    title = StringField()
    description = StringField()
    follow_up_responses = EmbeddedDocumentListField('Response')

class Entry(EmbeddedDocument):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    date = StringField()
    standard_responses = EmbeddedDocumentListField(Response)
    symptom_tile_responses = EmbeddedDocumentListField(Response)
    doctor_responses = EmbeddedDocumentListField(DoctorResponse)
    qb_responses = EmbeddedDocumentListField(Response)

class Surgery(Document):
    oid = IntField(required=True, primary_key=True)
    status = EnumField(Status)
    entries = EmbeddedDocumentListField(Entry)
    questionnaire = ReferenceField(Questionnaire, unique = False)
    symptom_tile_questionnaire = ReferenceField(SymptomTileQuestionnaire, unique = False)
    qb_questions = ListField(ReferenceField(QB_Question, unique = False))
    current_doctor_questions = ListField(StringField())
    patient = ReferenceField(Patient)
    
class User(Document):
    oid = IntField(required=True, primary_key=True)
    surgeries = ListField(ReferenceField(Surgery))