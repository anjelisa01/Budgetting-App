from pydantic import EmailStr,BaseModel,ConfigDict
from typing import Optional

#base
class UserBase(BaseModel)
    name:str
    email:EmailStr

#Input user
class UserCreate(UserBase):
    hashed_password:str
class UserUpdate(BaseModel):
    name:Optional[str]
    email:Optional[str]
    model_config = ConfigDict(from_attributes=True)

#output system
class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)

