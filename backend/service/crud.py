from sqlalchemy.orm import Session
from sqlalchemy import select

from models.models import User, Transaction
from schemas.schemas import TransactionAdd




def add_transaction(db:Session,transaction:TransactionAdd):
    db_transaction=Transaction(**transaction.model_dump())
    
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    
    return db_transaction

def get_all_transactions(db:Session):
    return db.scalars(select(Transaction)).all()
