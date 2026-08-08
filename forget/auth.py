#import 
from sqlalchemy.orm import Session

#schema auth
from schemas.auth import UserLogin

#security utils
from security import get_user_by_email,verify_password,create_access_token

#logger
from logger import logger

#exceptions
from exceptions import AuthFailedCredential

def login(db:Session,user:UserLogin):
    existed_user=get_user_by_email(db,user.email)
    '''
        user provide their credential : email and password
            if credential correct - success
            if credential wrong - failed
                exception when credential is wrong, im not gonna tell which one is wrong for security
    '''
    if not existed_user or not verify_password(db,user.password,existed_user.hashed_password):
        logger.warning("Attempt login with invalid credential")
        raise AuthFailedCredential()

    token=create_access_token({"user_id":str(existed_user.id)})

    logger.info("User created token. user_id=%s", existed_user.id)

    return {"access_token":token,"token-type":"bearer"}

    #this is how existed_user looks like
        # {
        # "email": "anjel@gmail.com",
        # "name": "tri",
        # "id": 2,
        # "hashed_password": "gsg655372"
        # }