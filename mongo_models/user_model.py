from mongoengine.document import EmbeddedDocument
from mongo_models.questionnaire_model import Questionnaire
from mongoengine import Document
from mongoengine.fields import EmbeddedDocumentListField, EnumField, IntField, ReferenceField
from mongoengine.fields import ListField, StringField, ObjectIdField
from enum import Enum, unique
from bson.objectid import ObjectId

class Status(Enum):
    ACTIVE = 'active'
    COMPLETE = 'complete'

class StandardResponse(EmbeddedDocument):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    question_id = StringField()
    response = StringField()

class DoctorResponse(EmbeddedDocument):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    question = StringField()
    response = StringField()

class Entry(EmbeddedDocument):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    date = StringField()
    standard_responses = EmbeddedDocumentListField(StandardResponse)
    doctor_responses = EmbeddedDocumentListField(DoctorResponse)

class Surgery(EmbeddedDocument):
    oid = IntField(required=True, primary_key=True)
    status = EnumField(Status)
    entries = EmbeddedDocumentListField(Entry)
    current_doctor_questions = ListField(StringField())
    questionnaire = ReferenceField(Questionnaire, unique = False)
    
class User(Document):
    oid = IntField(required=True, primary_key=True)
    surgeries = EmbeddedDocumentListField(Surgery)