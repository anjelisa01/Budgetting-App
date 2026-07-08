from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

#pydantic schemas
from schemas.transaction import TransactionAdd,TransactionResponse,TransactionUpdate


#services
from service.transaction import create_transaction,read_one_transaction,read_all_transaction,update_transaction,delete_transaction

#dependencies
from dependency import get_db,get_current_user

router=APIRouter(tags=["transactions"])

@router.post("/",response_model=TransactionResponse)
def add_transaction(transaction:TransactionAdd,user_id:int=Depends(get_current_user),db:Session=Depends(get_db)):
    return create_transaction(user_id,db,transaction)

#fixed path then dynamic path
@router.get("/",response_model=list[TransactionResponse])   
def get_all_transaction(user_id:int=Depends(get_current_user),db:Session=Depends(get_db)):
    return read_all_transaction(user_id,db)

@router.get("/{transaction_id}",response_model=TransactionResponse)
def get_one_transaction(transaction_id:int,user_id:int=Depends(get_current_user),db:Session=Depends(get_db)):  
    return read_one_transaction(user_id,transaction_id,db)


@router.patch("/{transaction_id}",response_model=TransactionResponse)
def edit_transaction(transaction_id:int,payload:TransactionUpdate,user_id:int=Depends(get_current_user), db:Session=Depends(get_db)):
    return update_transaction(user_id,transaction_id,db,payload)

@router.delete("/{transaction_id}")
def remove_transaction(transaction_id:int,user_id:int=Depends(get_current_user), db:Session=Depends(get_db)):
    return delete_transaction(user_id,transaction_id,db)