from pydantic import EmailStr,BaseModel,ConfigDict
from typing import Optional

class CategoryBase(BaseModel):
    category_name:str #same as account

class CategoryResponse(CategoryBase):
    id:int
