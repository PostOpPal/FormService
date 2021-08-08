from mongo_models.questionnaire_model import Questionnaire, Question
from mongoengine import Document, ObjectId
from mongoengine.fields import EmbeddedDocumentField, EnumField, ReferenceField
from mongoengine.fields import ListField, StringField, ObjectIdField
from enum import Enum


class Status(Enum):
    ACTIVE = 'active'
    COMPLETE = 'complete'

class StandardResponse(Document):
    _id = ObjectIdField(required=True, default=ObjectId, unique=True, primary_key=True)
    question = ReferenceField(Question)
    response = StringField()

class DoctorResponse(Document):
    _id = ObjectIdField(required=True, default=ObjectId, unique=True, primary_key=True)
    question = StringField()
    response = StringField()

class Entry(Document):
    _id = ObjectIdField(required=True, default=ObjectId, unique=True, primary_key=True)
    date = StringField()
    standard_responses = ListField(EmbeddedDocumentField(StandardResponse))
    doctor_responses = ListField(EmbeddedDocumentField(DoctorResponse))

class Surgery(Document):
    _id = ObjectIdField(required=True, default=ObjectId, unique=True, primary_key=True)
    status = EnumField(Status)
    entries = ListField(EmbeddedDocumentField(Entry))
    current_doctor_questions = ListField(StringField())
    questionnaire = ReferenceField(Questionnaire)
    
class User(Document):
    _id = ObjectIdField(required=True, default=ObjectId, unique=True, primary_key=True)
    surgeries = ListField(EmbeddedDocumentField(Surgery))