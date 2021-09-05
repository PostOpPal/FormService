from typing import Tuple
from mongo_models.user_model import MongoSurgery, MongoUser
from fastapi.exceptions import HTTPException


def get_user_and_surgery(user_id: str, surgery_id: str) -> Tuple[MongoUser,MongoSurgery]:
    try : user = MongoUser.objects(oid = user_id).first()
    except: raise HTTPException(status_code = 404, detail = "User not found")
    try : surgery = MongoSurgery.objects(oid = surgery_id).first()
    except: raise HTTPException(status_code = 404, detail = "Surgery not found")
    return user, surgery