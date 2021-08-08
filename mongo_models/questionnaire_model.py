from mongoengine import Document, ObjectId
from mongoengine.fields import EmbeddedDocumentField, EnumField, IntField, ListField, StringField, ObjectIdField
from enum import Enum


class Question_Type(Enum):
    TEXT = 'text'
    SCALE = 'scale'
    BOOLEAN = 'boolean'

class Question(Document):
    question_type = EnumField(Question_Type)
    _id = ObjectIdField(required=True, default=ObjectId, unique=True, primary_key=True)
    scale = StringField()
    text = StringField()

class Questionnaire(Document):
    _id = ObjectIdField(required=True, default=ObjectId, unique=True, primary_key=True)
    title = StringField()
    questions = ListField(EmbeddedDocumentField(Question))