#for custom rules
'''
so make sure the exception raised in service layer are not http tied
they should be only exception from python, and we handle with translating to http response in handler.py OR wherever
'''
class ResourceNotFoundError(Exception):
    def __init__(self, resource: str, identifier):
        self.resource = resource
        self.identifier = identifier
        super().__init__(f"{resource} not found: {identifier}")
# how to raised
# raise NotFoundError("Account", account_id)

class ResourceExistedError(Exception):
    def __init__(self, resource: str, identifier):
        self.resource = resource
        self.identifier = identifier
        super().__init__(f"{resource} already existed: {identifier}")





#custom exceptions
#for auth service
class AuthFailedCredential(Exception): #
    pass

#for user service
class UserAlreadyExisted(Exception):
    def __init__(self, email: str):
        self.email = email
    

#for transaction service
class TransactionNotFound(Exception):
    pass

class TransactionsEmpty(Exception):
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