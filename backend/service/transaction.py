#import
from sqlalchemy.orm import Session
from sqlalchemy import select

#sqlalchemy model: Transaction
from models.transaction import Transaction #,Category
from models.account import Account
#pydantic schemas: transaction
from schemas.transaction import TransactionAdd,TransactionResponse,TransactionUpdate

#logger
from logger import logger

#exceptions
from exceptions import TransactionNotFound

#CRUD ENDPOINT "/transaction"
def create_transaction(
    user_id:int,
    account_id:int,
    db:Session,
    transaction:TransactionAdd):

    #auth check using account_id and user_id
    account = (
        db.query(Account)
        .filter(
            Account.id == account_id,
            Account.user_id == user_id,
        )
        .first()
    )

    #build transaction
    db_transaction=Transaction(**transaction.model_dump())
    db_transaction.account_id=account_id

    #insert
    db.add(db_transaction)
    db.commit()
    logger.info("Transaction created, transaction id=%s",db_transaction.id)

    db.refresh(db_transaction)
    return db_transaction

def read_one_transaction(user_id:int,account_id:int,transaction_id:int,db:Session):
    #find account by the user id (auth check)
    account = (
        db.query(Account)
        .filter(
            Account.id == account_id,
            Account.user_id == user_id,
        )
        .first()
    )
    #exception

    #transaction data retrieval from the account table
    transaction = db.scalar(
        select(Transaction).where(
            Transaction.account_id==account.id,
            Transaction.id==transaction_id 
        ) 
    )
    #exception
    if not transaction:
        raise TransactionNotFound()

    return transaction

    
def read_all_transaction(user_id:int,account_id:int,db:Session):
    #read all transaction from an account
    
    #auth check
    account = (
        db.query(Account)
        .filter(
            Account.id == account_id,
            Account.user_id == user_id,
        )
        .first()
    )

    return db.scalars( #retrieve all transaction from table transaction where the account_id ==  account.id
        select(Transaction).where(Transaction.account_id == account.id)
    ).all()

    
def update_transaction(user_id:int,account_id:int,transaction_id:int,db:Session,payload:TransactionUpdate):
    #auth check comparing account.user_id== user_id
    account = (
        db.query(Account)
        .filter(
            Account.id == account_id,
            Account.user_id == user_id,
        )
        .first()
    )

    #find the transaction
    transaction = db.scalar(
        select(Transaction).where(
            Transaction.account_id==account.id,
            Transaction.id==transaction_id
        )
    )

    #update data
    update_data=payload.model_dump(exclude_unset=True)
    
    for field,value in update_data.items():
        setattr(transaction,field,value)

    db.commit()
    logger.info("Transaction updated, transaction_id=%s", transaction_id)

    db.refresh(transaction)

    return transaction

def delete_transaction(user_id:int,account_id:int,transaction_id:int,db:Session):
    #auth check comparing account.user_id== user_id
    account = (
        db.query(Account)
        .filter(
            Account.id == account_id,
            Account.user_id == user_id,
        )
        .first()
    )

    #find the transaction
    transaction = db.scalar(
        select(Transaction).where(
            Transaction.account_id==account.id,
            Transaction.id==transaction_id
        )
    )
    
    #delete
    db.delete(transaction)
    db.commit()
    logger.info("Transaction deleted.  on account_id=%s", account_id)
    return{"message":"deleted"}
