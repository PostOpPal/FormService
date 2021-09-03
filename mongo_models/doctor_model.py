from bson.objectid import ObjectId
from mongoengine.base.fields import ObjectIdField
from mongo_models.user_model import Surgery, User
from mongoengine import Document
from mongoengine.fields import IntField, ListField, ReferenceField

class Patient(Document):
    '''References an single surgery of a user'''
    oid = ObjectIdField(required=True, default = ObjectId, primary_key=True)
    user = ReferenceField(User)
    surgery = ReferenceField(Surgery)
    
class Doctor(Document):
    oid = IntField(required=True, primary_key=True)
    patients = ListField(ReferenceField(Patient))

