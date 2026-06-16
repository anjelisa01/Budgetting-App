#import
from sqlalchemy.orm import Session
from sqlalchemy import select

#sqlalchemy model: User
from models.all_models import User

#pydantic schemas: user
from schemas.user import UserCreate,UserUpdate

#security utils
from security import hash_password,get_user_by_email

#logger
from logger import logger

#exceptions
from exceptions import UserAlreadyExisted

# CRUD ENDPOINT "/users" for REGULAR USER
#-----------------------------------------
#create new user (sign up)
def create_user(db:Session, user:UserCreate):
    existing=get_user_by_email(db,user.email)

    if existing:
        logger.warning("attempt signup with existing user email")
        raise UserAlreadyExisted()

    db_user=User(**user.model_dump())
    db_user.hashed_password=hash_password(db_user.hashed_password)

    db.add(db_user)
    db.commit()
    logger.info("User created, user_id=%s", db_user.id)

    db.refresh(db_user) 
    return db_user
    

#read their data
def read_one_user(db:Session,user_id:int):
    #i dont think i need exception here, because if user already authenticated
    #the user data is definetely already existed
    return db.scalar(
        select(User).where(User.id==user_id)
    )

#update their data
def update_user(db:Session,user_id:int,payload:UserUpdate):
    stmt=select(User).where(User.id==user_id)
    user=db.scalar(stmt)
    update_data=payload.model_dump(exclude_unset=True)
    
    for field,value in update_data.items():
        setattr(user,field,value)

    db.commit()
    logger.info("User updated, user_id=%s", user_id)

    db.refresh(user)

    return user

#delete user
def delete_user(db:Session,user_id:int):
    stmt=select(User).where(User.id==user_id)
    user=db.scalar(stmt)

    db.delete(user)
    db.commit()
    logger.info("User deleted.  user_id=%s", user_id)

    return{"message":"deleted"}