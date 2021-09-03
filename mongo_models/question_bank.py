from mongoengine import Document
from mongoengine.fields import EnumField, StringField, ObjectIdField
from enum import Enum
from bson.objectid import ObjectId


class QB_Question_Type(Enum):
    TEXT = 'text'
    SCALE = 'scale'
    BOOLEAN = 'boolean'
    
class QB_Question(Document):
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    question_type = EnumField(QB_Question_Type)
    scale = StringField()
    text = StringField()