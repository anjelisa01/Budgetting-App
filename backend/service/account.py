from sqlalchemy.orm import Session
from sqlalchemy import select
from models.account import Account

from schemas.account import AccountBase
from logger import logger

def create_account(user_id:int,db:Session,account:AccountBase):
    #add user_id to the data to insert to db
    db_account=Account(**account.model_dump())
    db_account.user_id=user_id
    db.add(db_account)
    db.commit()
    logger.info("New Account created, account name=%s",db_account.account_name)

    db.refresh(db_account)
    return db_account

def read_one_account(user_id:int,account_id:int,db:Session):
    db_account=db.scalar(
        select(Account).where(
            Account.user_id==user_id,
            Account.id==account_id)
    )
    return db_account

def read_all_accounts(user_id:int,db:Session):
    return db.scalars(
        select(Account).where(Account.user_id == user_id)
    ).all()

def update_account(user_id:int,account_id:int,db:Session,payload:AccountBase):
    stmt=select(Account).where(
        Account.user_id==user_id,
        Account.id==account_id)
    account=db.scalar(stmt)
    update_data=payload.model_dump(exclude_unset=True)
    
    for field,value in update_data.items():
        setattr(account,field,value)

    db.commit()
    logger.info("Account updated, transaction name changes to =%s", account_id)

    db.refresh(account)

    return account

def delete_account(user_id:int,account_id:int,db:Session):
    stmt=select(Account).where(
        Account.user_id==user_id,
        Account.id==account_id)
    account=db.scalar(stmt)
    db.delete(account)
    db.commit()
    logger.info("Account deleted.  account name=%s", account.account_name) #supposed to be account_id
    return{"message":"deleted"}

