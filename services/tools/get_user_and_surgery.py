from mongo_models.user_model import Surgery, User
from fastapi.exceptions import HTTPException


def get_user_and_surgery(user_id: str, surgery_id: str):
    try : user : User = User.objects(oid = user_id).first()
    except: raise HTTPException(status_code = 404, detail = "User not found")
    try : surgery : Surgery = user.surgeries.get(oid = surgery_id)
    except : raise HTTPException(status_code = 404, detail = "Surgery not found")
    return user, surgery