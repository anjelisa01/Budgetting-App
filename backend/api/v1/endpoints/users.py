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

