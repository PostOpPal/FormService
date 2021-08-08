from mongoengine import Document
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import EmbeddedDocumentListField, EnumField, StringField, ObjectIdField
from enum import Enum
from bson.objectid import ObjectId


class Question_Type(Enum):
    TEXT = 'text'
    SCALE = 'scale'
    BOOLEAN = 'boolean'

class Question(EmbeddedDocument):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    question_type = EnumField(Question_Type)
    scale = StringField()
    text = StringField()

class Questionnaire(Document):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    title = StringField()
    questions = EmbeddedDocumentListField(Question)