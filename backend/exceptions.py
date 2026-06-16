#for custom rules
'''
so make sure the exception raised in service layer are not http tied
they should be only exception from python, and we handle with translating to http response in handler.py OR wherever
'''

#custom exceptions
#for auth service
class AuthFailedCredential(Exception): #
    pass

#for user service
class UserAlreadyExisted(Exception):
    pass











# =======================================================

# # auth service
# class AuthError(HTTPException): #named httpexceptions, the srvice layer that use this still depend on the http/aplication layer
#     pass

# class AuthFailedCredential(AuthError):
#     def __init__(self,message:str="invalid credential"):
#         super().__init__(status_code=401,detail=message)


# #user service
# class UserError(HTTPException):
#     pass
# class UserAlreadyExists(UserError):
#     def __init__(self,email:str):
#         self.email=email