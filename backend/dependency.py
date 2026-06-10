#==============================dependency injection for db session========================================
from database import SessionLocal
def get_db():
    db=SessionLocal()

    try:
        yield db
    finally:
        db.close()

#==============================dependecy injection for jwt decoding=====================================
from jose import jwt,JWTError #pip install
from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
import os 
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY")

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/login")

from sqlalchemy.orm import Session
from sqlalchemy import select
from models.all_models import User

def get_current_user(db:Session=Depends(get_db),token:str=Depends(oauth2_scheme)):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms='HS256')
        user_id=payload.get("user_id")
        user=db.scalar(select(User).where(User.id==user_id))
        return user.id
    except JWTError:
        raise HTTPException(status_code=401,detail="invalid token")