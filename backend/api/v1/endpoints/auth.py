from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

#pydantic schemas
from schemas.auth import UserLogin                                                      

#services
from service.auth import (login)

#exception handler:fastapi (app level)
from fastapi import HTTPException

#exception
from exceptions import AuthFailedCredential

#dependencies
from dependency import get_db

router=APIRouter(tags=["auth"])

@router.post("/login")
def auth_login(user:UserLogin,db:Session=Depends(get_db)):
    try: 
        return login(db,user)
    except AuthFailedCredential:
        raise HTTPException(
            status_code=401,
            detail="Failed credential"
        )
