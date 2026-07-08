from pydantic import BaseModel,ConfigDict
from typing import Optional

#Input user
class TransactionAdd(BaseModel):
    title:str
    amount:float
    note:str
    
class TransactionUpdate(BaseModel):
    title:str | None = None 
    amount:float | None = None
    note:str | None=None
    model_config = ConfigDict(from_attributes=True)
#output system
class TransactionResponse(TransactionAdd):
    model_config = ConfigDict(from_attributes=True)
