from fastapi import FastAPI

#logger
from logger import logger

from contextlib import asynccontextmanager

from database import Base
from database import engine

from api.v1.router import api_router

Base.metadata.create_all(bind=engine) #Models → DB (DB is generated from models)

# @asynccontextmanager
# async def lifespan(app:FastAPI):
#     logger.info("Aplication started")
#     yield
#     logger.info("Application stopped")

# app=FastAPI(lifespan=lifespan)

app=FastAPI()

app.include_router(api_router, prefix="/api/v1")








# from exceptions import UserAlreadyExists
# from handler import user_exists_handler

# app.add_exception_handler(
#     UserAlreadyExists,
#     user_exists_handler
# )






#=====================================

# #import
# from fastapi import FastAPI
# from fastapi import Depends
# from sqlalchemy.orm import Session

# from database import Base
# from database import engine

# # from schemas.schemas import(
# #     TransactionAdd,TransactionResponse
# # # )
# # from service.crud import(
# #     add_transaction,get_all_transactions
# # )

# #pydantic schemas
# from schemas.user import (UserCreate,UserResponse,UserUpdate)
# from schemas.auth import UserLogin

# #services
# from service.user import (create_user,read_one_user,update_user,delete_user)
# from service.auth import (login)

# #dependencies
# from dependency import get_db,get_current_user

# Base.metadata.create_all(bind=engine) #Models → DB (DB is generated from models)

# app=FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Hello World"}

# @app.post("/login")
# def auth_login(user:UserLogin,db:Session=Depends(get_db)):
#     return login(db,user)

# @app.post("/signup", response_model=UserResponse)
# def add_user(user:UserCreate, db:Session=Depends(get_db)):
#     return create_user(db,user)

# @app.get("/users/me/{user_id}",response_model=UserResponse)
# def get_one_user(user_id:int,db:Session=Depends(get_db)):
#     return read_one_user(db,user_id)

# @app.delete("/users/me/{user_id}")
# def remove_user(user_id:int,db:Session=Depends(get_db)):
#     return delete_user(db,user_id)

# @app.patch("/user/me/{user_id}",response_model=UserResponse)
# def edit_user(user_id:int, payload:UserUpdate,db:Session=Depends(get_db)):
#     return update_user(db,user_id,payload)



# # @app.post("/transactions",response_model=TransactionAdd)
# # def create_transaction(transaction:TransactionAdd,db:Session=Depends(get_db)):
# #     return add_transaction(db,transaction)

# # @app.get("/transactions",response_model=list[TransactionResponse])
# # def read_all_transactions(db:Session=Depends(get_db)):
# #     return get_all_transactions(db)


# #protected_user
# @app.get("/protected_user")
# def hello(db:Session=Depends(get_db),user_id:int=Depends(get_current_user)):
#     # return {"message":"success"}
#     return read_one_user(db,user_id)

