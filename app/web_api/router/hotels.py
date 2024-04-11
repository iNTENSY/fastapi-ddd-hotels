from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import inject, DishkaRoute
from fastapi import APIRouter, Depends, HTTPException
from http import HTTPStatus

from app.application.contracts.hotels.create_hotel_request import CreateHotelRequest
from app.application.contracts.hotels.delete_hotels_request import DeleteHotelRequest
from app.application.contracts.hotels.get_hotels_request import GetHotelRequest, GetHotelListRequest
from app.application.contracts.hotels.hotels_response import HotelsListResponse, HotelResponse
from app.application.contracts.hotels.update_hotels_request import UpdateHotelRequest
from app.application.usecase.hotels.create_hotel import CreateHotelUseCase
from app.application.usecase.hotels.delete_hotel import DeleteHotelUseCase
from app.application.usecase.hotels.get_hotel import GetHotelsUseCase, GetHotelUserCase
from app.application.usecase.hotels.update_hotel import UpdateHotelUseCase

router = APIRouter(prefix="/api/hotels", tags=["Hotels"], route_class=DishkaRoute)


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
    response = await get_hotel_interactor(get_hotel_request)
    if response is None:
        raise HTTPException(detail="Данного отеля не существует", status_code=HTTPStatus.NOT_FOUND)
    return response


@router.post(path="/", response_model=HotelResponse)
@inject
async def create_hotel(
        create_hotel_request: CreateHotelRequest,
        create_hotel_interactor: FromDishka[CreateHotelUseCase]
) -> HotelResponse:
    return await create_hotel_interactor(create_hotel_request)


@router.delete(path="/{id}", response_model=HotelResponse)
@inject
async def delete_hotel(
        delete_hotel_request: Annotated[DeleteHotelRequest, Depends()],
        delete_hotel_interactor: FromDishka[DeleteHotelUseCase]
) -> HotelResponse:
    response = await delete_hotel_interactor(delete_hotel_request)
    if response is None:
        raise HTTPException(detail="Данного отеля не существует", status_code=HTTPStatus.NOT_FOUND)
    return response


@router.patch(path="/{id}", response_model=HotelResponse)
@inject
async def update_hotel(
        id: int,
        update_hotel_request: UpdateHotelRequest,
        update_hotel_interactor: FromDishka[UpdateHotelUseCase]
) -> HotelResponse:
    response = await update_hotel_interactor(update_hotel_request, id=id)
    if response is None:
        raise HTTPException(detail="Данного отеля не существует", status_code=HTTPStatus.NOT_FOUND)
    return response
