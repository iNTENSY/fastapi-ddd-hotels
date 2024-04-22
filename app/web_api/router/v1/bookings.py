from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, Depends
from starlette.requests import Request

from app.application.contracts.bookings.booking_response import BookingResponse
from app.application.contracts.bookings.create_booking_request import (
    CreateBookingRequest,
)
from app.application.protocols.jwt_processor import JwtTokenProcessor
from app.application.usecase.bookings.create_booking import CreateBookingUseCase
from app.domain.users.errors import InvalidTokenError
from app.infrastructure.authentication.permissions import auth_required
from app.web_api.schemas.bookings import CreateBookingSchema

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.post("/", response_model=BookingResponse, dependencies=[Depends(auth_required)])
@inject
async def create_bookings(
    request: Request,
    create_bookings_request: CreateBookingSchema,
    interactor: FromDishka[CreateBookingUseCase],
    token_processor: FromDishka[JwtTokenProcessor],
) -> BookingResponse:
    token = request.scope.get("auth")
    payload = await token_processor.validate_token(token)
    if payload is None:
        raise InvalidTokenError
    response = await interactor(CreateBookingRequest(user_id=payload[0].value, content=create_bookings_request))
    return response
