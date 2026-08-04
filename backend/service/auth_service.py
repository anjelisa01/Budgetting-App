#import
from sqlalchemy.orm import Session
from sqlalchemy import select
from schemas.auth import UserLogin

#security utils
from security import get_user_by_email,verify_password,create_access_token

from logger import logger

class AuthService:
    def __init__(self,db: Session):
        self.db = db
    def login(self,payload:UserLogin):
        existed_user=get_user_by_email(self.db,payload.email)
        #expected warning
        try:
            token=create_access_token({"user_id":str(existed_user.id)})
        except Exception:
            raise
        logger.info("User created token. user_id=%s", existed_user.id)
        return {"access_token":token,"token-type":"bearer"}
