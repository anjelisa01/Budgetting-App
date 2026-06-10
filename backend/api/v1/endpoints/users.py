from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

#pydantic schemas
from schemas.user import UserCreate,UserResponse,UserUpdate                                                      

#services
from service.user import create_user,read_one_user,update_user,delete_user

#dependencies
from dependency import get_db,get_current_user

router=APIRouter(tags=["users"])

@router.post("/signup", response_model=UserResponse)
def add_user(user:UserCreate, db:Session=Depends(get_db)):
    return create_user(db,user)

@router.get("/me",response_model=UserResponse)
def get_one_user(user_id:int=Depends(get_current_user),db:Session=Depends(get_db)):
    return read_one_user(db,user_id)

@router.delete("/me")
def remove_user(user_id:int=Depends(get_current_user),db:Session=Depends(get_db)):
    return delete_user(db,user_id)

@router.patch("/me",response_model=UserResponse)
def edit_user(payload:UserUpdate,user_id:int=Depends(get_current_user), db:Session=Depends(get_db)):
    return update_user(db,user_id,payload)

#test curl: get current user data
'''
curl -X GET "https://friendly-doodle-x5wp79r55w9wfpj4x-8000.app.github.dev/api/v1/users/me" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMTUiLCJleHAiOjE3ODEwNjczNzN9.jQp1FsdSPjETdUe4eXRwPcAIgd9cXCFMv2Vpzh90Ylg"

'''