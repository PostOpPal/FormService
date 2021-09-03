from mongoengine import Document
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import EmbeddedDocumentListField, EnumField, ListField, StringField, ObjectIdField
from enum import Enum
from bson.objectid import ObjectId


class Question_Type(Enum):
    TEXT = 'text'
    SCALE = 'scale'
    BOOLEAN = 'boolean'

class Question(EmbeddedDocument):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    question_type = EnumField(Question_Type, required = True)
    text = StringField(required = True)
    scale = StringField()
    options = ListField()
    follow_up_questions = ListField(ListField('Question'))

class Questionnaire(Document):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    title = StringField()
    questions = EmbeddedDocumentListField(Question)

class SymptomTile(EmbeddedDocument):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    logo = StringField()
    title = StringField(required = True)
    follow_up_questions = EmbeddedDocumentListField(Question)

class SymptomTileQuestionnaire(Document):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    title = StringField(required = True)
    tiles = EmbeddedDocumentListField(SymptomTile)