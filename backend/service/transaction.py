#import
from sqlalchemy.orm import Session
from sqlalchemy import select

#sqlalchemy model: Transaction
from models.all_models import Transaction

#pydantic schemas: transaction
from schemas.transaction import TransactionAdd,TransactionResponse,TransactionUpdate

#logger
from logger import logger


#exceptions


#CRUD ENDPOINT "/transaction"

def create_transaction(user_id:int,db:Session,transaction:TransactionAdd):
    db_transaction=Transaction(**transaction.model_dump())
    db_transaction.user_id=user_id
    db.add(db_transaction)
    db.commit()
    logger.info("Transaction created, transaction id=%s",db_transaction.id)

    db.refresh(db_transaction)
    return db_transaction

def read_one_transaction(user_id:int,transaction_id:int,db:Session):
    #read one transaction information
    #read one by its id
    return db.scalar(
        select(Transaction).where(
            Transaction.user_id==user_id,
            Transaction.id==transaction_id)
    )
    
def read_all_transaction(user_id:int,db:Session):
    #read all transaction from current user
    return db.scalars(
        select(Transaction).where(Transaction.user_id == user_id)
    ).all()

def update_transaction(user_id:int,transaction_id:int,db:Session,payload:TransactionUpdate):
    stmt=select(Transaction).where(
        Transaction.user_id==user_id,
        Transaction.id==transaction_id)
    transaction=db.scalar(stmt)
    update_data=payload.model_dump(exclude_unset=True)
    
    for field,value in update_data.items():
        setattr(transaction,field,value)

    db.commit()
    logger.info("Transaction updated, transaction_id=%s", transaction_id)

    db.refresh(transaction)

    return transaction

def delete_transaction(user_id:int,transaction_id:int,db:Session):
    stmt=select(Transaction).where(
        Transaction.user_id==user_id,
        Transaction.id==transaction_id)
    transaction=db.scalar(stmt)
    db.delete(transaction)
    db.commit()
    logger.info("Transaction deleted.  user_id=%s", transaction_id)
    return{"message":"deleted"}