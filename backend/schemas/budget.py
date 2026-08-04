from pydantic import EmailStr,BaseModel,ConfigDict
from typing import Optional

class BudgetBase(BaseModel):
    limit:float
    period:str
    
    # category_id:int

class BudgetUpdate(BaseModel):
    limit:float  | None = None
    period:str  | None = None