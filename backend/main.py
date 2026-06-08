from fastapi import FastAPI
from fastapi import Depends

from sqlalchemy.orm import Session

from database import Base
from database import SessionLocal
from database import engine

from schemas.schemas import(
    TransactionAdd,TransactionResponse
)
from service.crud import(
    add_transaction,get_all_transactions
)


from schemas.users_schemas import (UserCreate,UserResponse,UserUpdate)
from service.users_service import (create_user,read_one_user,update_user,delete_user)

Base.metadata.create_all(bind=engine) #Models → DB (DB is generated from models)

app=FastAPI()

#dependency injection for db session
def get_db():
    db=SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/signup", response_model=UserResponse)
def add_user(user:UserCreate, db:Session=Depends(get_db)):
    return create_user(db,user)

@app.get("/users/me/{user_id}",response_model=UserResponse)
def get_one_user(user_id:int,db:Session=Depends(get_db)):
    return read_one_user(db,user_id)

@app.delete("/users/me/{user_id}")
def remove_user(user_id:int,db:Session=Depends(get_db)):
    return delete_user(db,user_id)

@app.patch("/user/me/{user_id}",response_model=UserResponse)
def edit_user(user_id:int, payload:UserUpdate,db:Session=Depends(get_db)):
    return update_user(db,user_id,payload)

@app.post("/transactions",response_model=TransactionAdd)
def create_transaction(transaction:TransactionAdd,db:Session=Depends(get_db)):
    return add_transaction(db,transaction)

@app.get("/transactions",response_model=list[TransactionResponse])
def read_all_transactions(db:Session=Depends(get_db)):
    return get_all_transactions(db)