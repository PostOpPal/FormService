from typing import List
from models.generated_models.responses.questionnaire_response import Question
from mongoengine import Document
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import EmbeddedDocumentField, EmbeddedDocumentListField, EnumField, ListField, ReferenceField, StringField, ObjectIdField
from enum import Enum
from bson.objectid import ObjectId


class QB_Question_Type(Enum):
    TEXT = 'text'
    SCALE = 'scale'
    BOOLEAN = 'boolean'
    OPTIONS = 'options'
    RADIO = 'radio'

class QB_Question(Document):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    tags = ListField(StringField())
    question = EmbeddedDocument(Question)