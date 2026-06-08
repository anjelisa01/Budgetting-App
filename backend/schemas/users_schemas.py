from pydantic import BaseModel,ConfigDict
from typing import Optional

#Input user
class UserCreate(BaseModel):
    name:str
    email:str
    hashed_password:str
class UserUpdate(BaseModel):
    name:Optional[str]
    email:Optional[str]
    model_config = ConfigDict(from_attributes=True)

#output system
class UserResponse(UserCreate):
    model_config = ConfigDict(from_attributes=True)

