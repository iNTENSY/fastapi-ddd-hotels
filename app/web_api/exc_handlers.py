from http import HTTPStatus

from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse

from app.domain.common.errors import DomainValidationError
from app.domain.hotels.errors import HotelNotFound


async def validation_error_exc_handler(request: Request, exc: DomainValidationError):
    return JSONResponse(content={"detail": exc.message}, status_code=HTTPStatus.UNPROCESSABLE_ENTITY)


async def hotel_not_found_exc_handler(request: Request, exc: HotelNotFound):
    return JSONResponse(content={"detail": exc.message}, status_code=HTTPStatus.NOT_FOUND)


def init_exc_handlers(app: FastAPI) -> None:
    """Exception handlers."""
    app.add_exception_handler(DomainValidationError, validation_error_exc_handler)
    app.add_exception_handler(HotelNotFound, hotel_not_found_exc_handler)
