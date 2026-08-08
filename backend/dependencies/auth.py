from jose import jwt,JWTError #pip install
from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
import os 
from dotenv import load_dotenv
load_dotenv()

from dependencies.database import get_db

SECRET_KEY=os.getenv("SECRET_KEY")

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

from sqlalchemy.orm import Session
from sqlalchemy import select
from models.user import User

def get_current_user(db:Session=Depends(get_db),token:str=Depends(oauth2_scheme)):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms='HS256')
        user_id=payload.get("user_id")
        user=db.scalar(select(User).where(User.id==user_id))
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return user.id
    except JWTError:
        raise HTTPException(status_code=401,detail="invalid token")