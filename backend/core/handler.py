from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
# from .exceptions import UserNotFound, DuplicateEmail
from core.exceptions import UserAlreadyExisted,ResourceNotFoundError,ResourceExistedError
from core.logger import logger

def register_handlers(app: FastAPI):
    @app.exception_handler(ResourceNotFoundError)
    async def resource_not_found_handler(request: Request, exc: ResourceNotFoundError):
        logger.info(
            "%s %s - %s not found (id=%s)",
            request.method,
            request.url.path,
            exc.resource,
            exc.identifier,
        )
        return JSONResponse(
            status_code=404,
            content={
                "error": "NOT_FOUND",
                "resource": exc.resource,
                "message": str(exc),
            },
        )
    @app.exception_handler(ResourceExistedError)
    async def resource_existed_handler(request: Request, exc: ResourceExistedError):
        logger.info(
            "%s %s - %s existed (id=%s)",
            request.method,
            request.url.path,
            exc.resource,
            exc.identifier,
        )
        return JSONResponse(
            status_code=409,
            content={
                "error": "EXISTED",
                "resource": exc.resource,
                "message": str(exc),
            },
        )




    @app.exception_handler(UserAlreadyExisted)
    async def user_already_exists_handler(request: Request, exc: UserAlreadyExisted):
        logger.info(
            "Signup failed: email already exists, email=%s",
            exc.email
        )
        return JSONResponse(
            status_code=409,
            content={"detail": "user already exists"},
        )
    @app.exception_handler(Exception)
    async def general_handler(request: Request, exc: Exception):
        logger.exception("Unhandled exception")  # includes traceback
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error"},
        )

    
    # @app.exception_handler(UserNotFound)
    # async def user_not_found_handler(request: Request, exc: UserNotFound):
    #     return JSONResponse(
    #         status_code=404,
    #         content={"detail": "User not found"},
    #     )

    # @app.exception_handler(DuplicateEmail)
    # async def duplicate_email_handler(request: Request, exc: DuplicateEmail):
    #     logger.warning(duplicate email")

    #     return JSONResponse(
    #         status_code=409,
    #         content={"detail": "duplicate email"},
    #     )

