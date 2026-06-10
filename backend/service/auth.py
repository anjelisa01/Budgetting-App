#import 
from fastapi import HTTPException
from sqlalchemy.orm import Session

#schema auth
from schemas.auth import UserLogin

#security utils
from security import get_user_by_email,verify_password,create_access_token

def login(db:Session,user:UserLogin):
    existed_user=get_user_by_email(db,user.email)

    if not existed_user or not verify_password(db,user.password,existed_user.hashed_password):
        raise HTTPException(status_code=401,detail="invalid credentials")
    token=create_access_token({"user_id":str(existed_user.id)})
    return {"access_token":token,"token-type":"bearer"}

    #this is how existed_user looks like
        # {
        # "email": "anjel@gmail.com",
        # "name": "tri",
        # "id": 2,
        # "hashed_password": "gsg655372"
        # }