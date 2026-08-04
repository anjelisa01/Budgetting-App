#import
from sqlalchemy.orm import Session
from sqlalchemy import select
#sqlalchemy model: Transaction
from models.transaction import Transaction #,Category
from models.account import Account
#pydantic schemas: transaction
from schemas.transaction import TransactionAdd,TransactionResponse,TransactionUpdate
#util
from exceptions import ResourceExistedError,ResourceNotFoundError
from logger import logger

def update_account_balance(account_id:int,transaction_type:str):
    '''
    account current_balance=10000
    user insert transaction data: 400, expense
    system update account current_balance:
        parameter(account_id,transaction)
        find account 
        if transaction.transaction_type==expense:
            account.current_balance= account.current_balance-transaction.amount
        if transaction.transaction_type==income:
            account.current_balance= account.current_balance+transaction.amount
    '''

class TransactionService:
    def __init__(self,db: Session,user_id:int):
        self.db = db
        self.user_id=user_id
    def create(self,account_id:int,payload:TransactionAdd):
        #find account 
        account = (
            self.db.query(Account)
            .filter(
                Account.id == account_id,
                Account.user_id == self.user_id,
            )
            .first()
        )
        if account is None:
            raise ResourceNotFoundError("Account", account_id)

        #build transaction data
        transaction=Transaction(**payload.model_dump())
        transaction.account_id=account.id

        #update account balance
        if transaction.transaction_type=="expense":
            account.current_balance=account.current_balance - transaction.amount
        if transaction.transaction_type=="income":
            account.current_balance=account.current_balance + transaction.amount
       

        #if category not set, input null to db
        if transaction.category_id==0:
            transaction.category_id=None
            
        #insert
        try:
            self.db.add(transaction)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise 
        logger.info("Transaction created, transaction id=%s", transaction.id)
        self.db.refresh(transaction)
        return transaction
    def read_one(self,account_id:int,transaction_id:int):
        #find account 
        account = (
            self.db.query(Account)
            .filter(
                Account.id == account_id,
                Account.user_id == self.user_id,
            )
            .first()
        )
        if account is None:
            raise ResourceNotFoundError("Account", account_id)
        
        # find the transaction
        transaction= self.db.scalar(
            select(Transaction).where(
                Transaction.account_id==account.id,
                Transaction.id==transaction_id 
            ) 
        )
        if transaction is None:
            raise ResourceNotFoundError("Transaction", transaction_id)
        return transaction

    def read_all(self,account_id:int):
        #find account 
        account = (
            self.db.query(Account)
            .filter(
                Account.id == account_id,
                Account.user_id == self.user_id,
            )
            .first()
        )
        if account is None:
            raise ResourceNotFoundError("Account", account_id)

        return self.db.scalars( #retrieve all transaction from table transaction where the account_id ==  account.id
            select(Transaction).where(Transaction.account_id == account.id)
        ).all()
       
    def update(self,account_id:int,transaction_id:int,payload:TransactionUpdate):
        account = (
            self.db.query(Account)
            .filter(
                Account.id == account_id,
                Account.user_id == self.user_id,
            )
            .first()
        )
        if account is None:
            raise ResourceNotFoundError("Account", account_id)

        # find the transaction
        transaction = self.db.scalar(
            select(Transaction).where(
                Transaction.account_id==account.id,
                Transaction.id==transaction_id 
            ) 
        )
    
        if transaction is None:
            raise ResourceNotFoundError("Transaction", transaction_id)
        #build update data
        update_data=payload.model_dump(exclude_unset=True)
        
        
        if update_data["amount"]:
            #changing amount
            difference=transaction.amount-update_data["amount"]        
            if transaction.transaction_type=="income":
                account.current_balance=account.current_balance - difference
                logger.info("current balance after update : %s",account.current_balance )
            if transaction.transaction_type=="expense":
                account.current_balance=account.current_balance + difference 
        
        #update
        try:
            for field,value in update_data.items():
                setattr(transaction,field,value)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise
        logger.info("Transaction updated, transaction id=%s", transaction_id)
        self.db.refresh(transaction)
        return transaction
    def delete(self,account_id:int,transaction_id:int):
        account = (
            self.db.query(Account)
            .filter(
                Account.id == account_id,
                Account.user_id == self.user_id,
            )
            .first()
        )
        if account is None:
            raise ResourceNotFoundError("Account", account_id)

        # find the transaction
        transaction = self.db.scalar(
            select(Transaction).where(
                Transaction.account_id==account.id,
                Transaction.id==transaction_id 
            ) 
        )
        if transaction is None:
            raise ResourceNotFoundError("Transaction", transaction_id)
        #delete
        try:
            self.db.delete(transaction)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise
        logger.info("Transaction deleted,  transaction id=%s", transaction_id) 
        return{"message":"deleted"}