from sqlalchemy.orm import Session
from sqlalchemy import select

from models.models import User
from schemas.users_schemas import UserCreate,UserUpdate

# CRUD ENDPOINT "/users" for REGULAR USER
#-----------------------------------------
#create new user (sign up)
def create_user(db:Session, user:UserCreate):
    db_user=User(**user.model_dump())

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

#read their data
def read_one_user(db:Session,user_id:int):
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
    db.refresh(user)

    return user

#delete their data
def delete_user(db:Session,user_id:int):
    stmt=select(User).where(User.id==user_id)
    user=db.scalar(stmt)

    db.delete(user)
    db.commit()

    return{"message":"deleted"}