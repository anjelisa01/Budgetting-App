from pydantic import BaseModel,ConfigDict
from typing import Optional

#Input user
class TransactionAdd(BaseModel):
    title:str
    amount:float
    note:str
    user_id:int

# class UserLogin(BaseModel):



#output system
class TransactionResponse(TransactionAdd):
    model_config = ConfigDict(from_attributes=True)
