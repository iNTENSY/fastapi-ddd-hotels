from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import inject, DishkaRoute
from fastapi import APIRouter, Depends
from starlette.requests import Request

from app.application.contracts.hotels.create_hotel_request import CreateHotelRequest
from app.application.contracts.hotels.delete_hotels_request import DeleteHotelRequest
from app.application.contracts.hotels.get_hotels_request import GetHotelRequest, GetHotelListRequest
from app.application.contracts.hotels.hotels_response import HotelsListResponse, HotelResponse
from app.application.contracts.hotels.update_hotels_request import UpdateHotelRequest
from app.application.usecase.hotels.create_hotel import CreateHotelUseCase
from app.application.usecase.hotels.delete_hotel import DeleteHotelUseCase
from app.application.usecase.hotels.get_hotel import GetHotelsUseCase, GetHotelUserCase
from app.application.usecase.hotels.update_hotel import UpdateHotelUseCase
from app.domain.hotels.errors import HotelNotFoundError
from app.domain.users.errors import InvalidTokenError
from app.infrastructure.authentication.jwt_processor import JwtTokenProcessorImp
from app.infrastructure.authentication.permissions import auth_required

router = APIRouter(prefix="/hotels", tags=["Hotels"], route_class=DishkaRoute)


@router.get(path="/", response_model=HotelsListResponse)
@inject
async def get_hotels(
        request: Annotated[GetHotelListRequest, Depends()],
        interactor: FromDishka[GetHotelsUseCase]
) -> HotelsListResponse:
    return await interactor(request)


@router.get(path="/{id}", response_model=HotelResponse)
@inject
async def get_hotel(
        get_hotel_request: Annotated[GetHotelRequest, Depends()],
        interactor: FromDishka[GetHotelUserCase],
) -> HotelResponse:
    response = await interactor(get_hotel_request)
    if response is None:
        raise HotelNotFoundError
    return response


@router.post(path="/", response_model=HotelResponse, dependencies=[Depends(auth_required)])
@inject
async def create_hotel(
        request: Request,
        create_hotel_request: CreateHotelRequest,
        interactor: FromDishka[CreateHotelUseCase],
        token_processor: FromDishka[JwtTokenProcessorImp]
) -> HotelResponse:
    if await token_processor.validate_token(request.scope["auth"]) is None:
        raise InvalidTokenError
    return await interactor(create_hotel_request)


@router.delete(path="/{id}", response_model=HotelResponse, dependencies=[Depends(auth_required)])
@inject
async def delete_hotel(
        request: Request,
        delete_hotel_request: Annotated[DeleteHotelRequest, Depends()],
        interactor: FromDishka[DeleteHotelUseCase],
        token_processor: FromDishka[JwtTokenProcessorImp]
) -> HotelResponse:
    if await token_processor.validate_token(request.scope["auth"]) is None:
        raise InvalidTokenError
    response = await interactor(delete_hotel_request)
    if response is None:
        raise HotelNotFoundError
    return response


@router.patch(path="/{id}", response_model=HotelResponse, dependencies=[Depends(auth_required)])
@inject
async def update_hotel(
        id: int,
        request: Request,
        update_hotel_request: UpdateHotelRequest,
        update_hotel_interactor: FromDishka[UpdateHotelUseCase],
        token_processor: FromDishka[JwtTokenProcessorImp]
) -> HotelResponse:
    if await token_processor.validate_token(request.scope["auth"]) is None:
        raise InvalidTokenError
    response = await update_hotel_interactor(update_hotel_request, id=id)
    if response is None:
        raise HotelNotFoundError
    return response
