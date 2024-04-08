from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, Depends

from app.application.contracts.hotels.get_hotels_request import GetHotelRequest, GetHotelListRequest
from app.application.contracts.hotels.hotels_response import HotelsListResponse
from app.application.usecase.hotels.get_hotel import GetHotelsUseCase


router = APIRouter(prefix="/hotels")

@router.get(path="/", response_model=HotelsListResponse)
@inject
async def get_hotels(
        get_hotel_list_request: Annotated[GetHotelListRequest, Depends()],
        get_hotel_list_interactor: FromDishka[GetHotelsUseCase]
):
    return await get_hotel_list_interactor(get_hotel_list_request)
