from mongoengine.document import EmbeddedDocument
from mongo_models.questionnaire_model import MongoQuestionType, MongoQuestionnaire, MongoSymptomQuestionnaire, MongoQBQuestion
from mongoengine import Document
from mongoengine.fields import EmbeddedDocumentListField, EnumField, IntField, ReferenceField
from mongoengine.fields import ListField, StringField, ObjectIdField
from enum import Enum
from bson.objectid import ObjectId

class MongoStatus(Enum):
    ACTIVE = 'active'
    COMPLETE = 'complete'

class MongoDoctorResponse(EmbeddedDocument):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    question = StringField()
    response = StringField()

class MongoResponse(EmbeddedDocument):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    question = StringField()
    question_type = EnumField(MongoQuestionType, required = True)
    scale = IntField()
    response = StringField()
    follow_up_responses = EmbeddedDocumentListField('MongoResponse')

class MongoSymptomResponse(EmbeddedDocument):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    title = StringField()
    description = StringField()
    follow_up_responses = EmbeddedDocumentListField(MongoResponse)

class MongoEntry(EmbeddedDocument):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    date = StringField()
    questionnaire_id = StringField()
    symptom_questionnaire_id = StringField()
    standard_responses = EmbeddedDocumentListField(MongoResponse)
    symptom_responses = EmbeddedDocumentListField(MongoSymptomResponse)
    doctor_responses = EmbeddedDocumentListField(MongoDoctorResponse)
    qb_responses = EmbeddedDocumentListField(MongoResponse)

class MongoSurgery(Document):
    oid = IntField(required=True, primary_key=True)
    status = EnumField(MongoStatus)
    entries = EmbeddedDocumentListField(MongoEntry)
    questionnaire = ReferenceField(MongoQuestionnaire, unique = False)
    symptom_questionnaire = ReferenceField(MongoSymptomQuestionnaire, unique = False)
    qb_questions = ListField(ReferenceField(MongoQBQuestion, unique = False))
    current_doctor_questions = ListField(StringField())
    patient = ReferenceField('MongoPatient')
    
class MongoUser(Document):
    oid = IntField(required=True, primary_key=True)
    surgeries = ListField(ReferenceField(MongoSurgery))

class MongoPatient(Document):
    '''References an single surgery of a user'''
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    user = ReferenceField(MongoUser)
    surgery = ReferenceField(MongoSurgery)
    
class MongoDoctor(Document):
    oid = IntField(required=True, primary_key=True)
    patients = ListField(ReferenceField(MongoPatient))