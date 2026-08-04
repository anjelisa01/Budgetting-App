from pydantic import EmailStr,BaseModel,ConfigDict
from typing import Optional
from decimal import Decimal

class AccountBase(BaseModel):
    account_name:str #in update this field is the only updatable so use this model directly is fine, dont need |none=none
    current_balance:Decimal
class AccountUpdate(BaseModel):
    current_balance:float  | None = None
    account_name:str  | None = None
class AccountResponse(AccountBase):
    id:int
    