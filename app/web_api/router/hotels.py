from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import inject, DishkaRoute
from fastapi import APIRouter, Depends

from app.application.contracts.hotels.get_hotels_request import GetHotelRequest, GetHotelListRequest
from app.application.contracts.hotels.hotels_response import HotelsListResponse, HotelResponse
from app.application.usecase.hotels.get_hotel import GetHotelsUseCase, GetHotelUserCase

router = APIRouter(prefix="/hotels", tags=["Hotels"], route_class=DishkaRoute)

@router.get(path="/", response_model=HotelsListResponse)
@inject
async def get_hotels(
        get_hotel_list_request: Annotated[GetHotelListRequest, Depends()],
        get_hotel_list_interactor: FromDishka[GetHotelsUseCase]
) -> HotelsListResponse:
    return await get_hotel_list_interactor(get_hotel_list_request)


@router.get(path="/{id}", response_model=HotelResponse)
@inject
async def get_hotel(
        get_hotel_request: Annotated[GetHotelRequest, Depends()],
        get_hotel_interactor: FromDishka[GetHotelUserCase]
) -> HotelResponse:
    return await get_hotel_interactor(get_hotel_request)

