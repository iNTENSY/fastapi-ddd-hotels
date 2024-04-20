from http import HTTPStatus

from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse

from app.domain.common.errors import DomainValidationError
from app.domain.hotels.errors import HotelNotFoundError
from app.domain.rooms.errors import RoomNotFoundError
from app.domain.users.errors import InvalidTokenError, UserNotFoundError, InvalidUserDataError, UserBadPermissionError


async def validation_error_exc_handler(request: Request, exc: DomainValidationError):
    return JSONResponse(content={"detail": exc.message}, status_code=HTTPStatus.UNPROCESSABLE_ENTITY)


async def hotel_not_found_exc_handler(request: Request, exc: HotelNotFoundError):
    return JSONResponse(content={"detail": exc.message}, status_code=HTTPStatus.NOT_FOUND)


async def user_not_found_exc_handler(request: Request, exc: UserNotFoundError):
    return JSONResponse(content={"detail": exc.message}, status_code=HTTPStatus.NOT_FOUND)


async def user_invalid_data_exc_handler(request: Request, exc: InvalidUserDataError):
    return JSONResponse(content={"detail": exc.message}, status_code=HTTPStatus.BAD_REQUEST)


async def user_bad_permission_exv_handler(request: Request, exc: UserBadPermissionError):
    return JSONResponse(content={"detail": exc.message}, status_code=HTTPStatus.FORBIDDEN)


async def jwt_invalid_exc_handler(request: Request, exc: InvalidTokenError):
    return JSONResponse(content={"detail": exc.message}, status_code=HTTPStatus.FORBIDDEN)


async def room_not_found_exc_handler(request: Request, exc: RoomNotFoundError):
    return JSONResponse(content={"detail": exc.message}, status_code=HTTPStatus.NOT_FOUND)


def init_exc_handlers(app: FastAPI) -> None:
    """Exception handlers."""
    app.add_exception_handler(DomainValidationError, validation_error_exc_handler)
    app.add_exception_handler(HotelNotFoundError, hotel_not_found_exc_handler)
    app.add_exception_handler(UserNotFoundError, user_not_found_exc_handler)
    app.add_exception_handler(InvalidUserDataError, user_invalid_data_exc_handler)
    app.add_exception_handler(UserBadPermissionError, user_bad_permission_exv_handler)
    app.add_exception_handler(InvalidTokenError, jwt_invalid_exc_handler)
    app.add_exception_handler(RoomNotFoundError, room_not_found_exc_handler)
