from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from starlette.requests import Request

from app.application.contracts.bookings.create_booking_request import CreateBookingRequest
from app.domain.users.errors import InvalidTokenError
from app.infrastructure.authentication.jwt_processor import JwtTokenProcessorImp

router = APIRouter(prefix="/bookings")


@router.post("")
@inject
async def get_bookings(
        request: Request,
        add_bookings_request: CreateBookingRequest,
        interactor: FromDishka[...],
        token_processor: FromDishka[JwtTokenProcessorImp]
):
    token = request.scope.get("auth")
    if await token_processor.validate_token(token) is None:
        raise InvalidTokenError
    response = await interactor(add_bookings_request)
    return response
