from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

#pydantic schemas
from schemas.auth import UserLogin                                                      

#services
from service.auth import (login)

#dependencies
from dependency import get_db

router=APIRouter(tags=["auth"])

@router.post("/login")
def auth_login(user:UserLogin,db:Session=Depends(get_db)):
    return login(db,user)