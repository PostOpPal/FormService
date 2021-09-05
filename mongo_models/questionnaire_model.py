from mongoengine import Document
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import EmbeddedDocumentField, EmbeddedDocumentListField, EnumField, ListField, ReferenceField, StringField, ObjectIdField
from enum import Enum
from bson.objectid import ObjectId


class MongoQuestionType(Enum):
    TEXT = 'text'
    SCALE = 'scale'
    BOOLEAN = 'boolean'
    OPTIONS = 'options'
    RADIO = 'radio'
    
class MongoQuestion(EmbeddedDocument):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    question_type = EnumField(MongoQuestionType, required = True)
    question = StringField(required = True)
    scale = StringField()
    options = ListField(StringField())
    follow_up_questions = ListField(EmbeddedDocumentListField('MongoQuestion'))

class MongoQBQuestion(Document):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    tags = ListField(StringField())
    question = EmbeddedDocumentField(MongoQuestion)

class MongoQuestionnaire(Document):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    title = StringField()
    questions = EmbeddedDocumentListField(MongoQuestion)

class MongoSymptomQuestion(EmbeddedDocument):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    logo = StringField()
    title = StringField(required = True)
    description = StringField()
    follow_up_questions = EmbeddedDocumentListField(MongoQuestion)

class MongoSymptomQuestionnaire(Document):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    title = StringField(required = True)
    questions = EmbeddedDocumentListField(MongoSymptomQuestion)