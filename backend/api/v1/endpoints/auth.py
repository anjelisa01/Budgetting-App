from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

#pydantic schemas
from schemas.auth import UserLogin                                                      

#exception handler:fastapi (app level)
from fastapi import HTTPException

#exception
from core.exceptions import AuthFailedCredential

# services
from service.auth_service import AuthService
#dependencies
from dependencies.services import get_auth_service


router=APIRouter(tags=["auth"])

@router.post("/login") #i changed from userlogin to authformbearer
def auth_login(form_data: OAuth2PasswordRequestForm = Depends(),service:AuthService=Depends(get_auth_service)):      #(form:UserLogin,service:AuthService=Depends(get_auth_service)):
    payload = UserLogin(
        email=form_data.username,  # Swagger username = your email
        password=form_data.password
    )
    try: 
        return service.login(payload)
    except AuthFailedCredential:
        raise HTTPException(
            status_code=401,
            detail="Failed credential"
        )
