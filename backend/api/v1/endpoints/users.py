from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

#pydantic schemas
from schemas.user import UserCreate,UserResponse,UserUpdate                                                      

#dependencies
from dependency import get_current_user

from service.user_service import UserService
from dependencies.services import get_user_service

#exception
from exceptions import UserAlreadyExisted

router=APIRouter(tags=["users"])

@router.post("/signup", response_model=UserResponse)
def add_user(payload:UserCreate, service: UserService = Depends(get_user_service)):
    return service.create(payload)

@router.get("/me",response_model=UserResponse)
def get_one_user(user_id:int=Depends(get_current_user),service: UserService = Depends(get_user_service)):
    return service.read_one(user_id)

@router.delete("/me")
def remove_user(user_id:int=Depends(get_current_user),service: UserService = Depends(get_user_service)):
    return service.delete(user_id)

@router.patch("/me",response_model=UserResponse)
def edit_user(payload:UserUpdate,user_id:int=Depends(get_current_user), service: UserService = Depends(get_user_service)):
    return service.update(user_id,payload)

