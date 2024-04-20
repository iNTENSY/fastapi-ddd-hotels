from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import inject, DishkaRoute
from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from starlette.requests import Request

from app.application.contracts.hotels.create_hotel_request import CreateHotelRequest
from app.application.contracts.hotels.delete_hotels_request import DeleteHotelRequest
from app.application.contracts.hotels.get_hotels_request import GetHotelRequest, GetHotelListRequest
from app.application.contracts.hotels.hotels_response import HotelsListResponse, HotelResponse
from app.application.contracts.hotels.update_hotels_request import UpdateHotelRequest
from app.application.contracts.rooms.create_room_request import CreateRoomRequest
from app.application.contracts.rooms.get_rooms_request import GetRoomsListRequest, GetRoomRequest
from app.application.contracts.rooms.rooms_response import RoomsListResponse, RoomResponse
from app.application.usecase.hotels.create_hotel import CreateHotelUseCase
from app.application.usecase.hotels.delete_hotel import DeleteHotelUseCase
from app.application.usecase.hotels.get_hotel import GetHotelsUseCase, GetHotelUserCase
from app.application.usecase.hotels.update_hotel import UpdateHotelUseCase
from app.application.usecase.rooms.create_room import CreateRoomUseCase
from app.application.usecase.rooms.get_room import GetRoomUseCase, GetRoomsUseCase
from app.domain.hotels.errors import HotelNotFoundError
from app.domain.rooms.errors import RoomNotFoundError
from app.domain.users.errors import InvalidTokenError
from app.infrastructure.authentication.jwt_processor import JwtTokenProcessorImp
from app.infrastructure.authentication.permissions import auth_required
from app.web_api.schemas.rooms import CreateRoomSchema

router = APIRouter(prefix="/hotels", tags=["Hotels"], route_class=DishkaRoute)


@router.get(path="/", response_model=HotelsListResponse)
@cache(expire=60*10)
@inject
async def get_hotels(
        get_hotels_request: Annotated[GetHotelListRequest, Depends()],
        interactor: FromDishka[GetHotelsUseCase]
) -> HotelsListResponse:
    return await interactor(get_hotels_request)


@router.get(path="/{id}", response_model=HotelResponse)
@cache(expire=60*5)
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


@router.get("/{id}/rooms", response_model=RoomsListResponse)
async def get_rooms_by_hotel_id(
        rooms_request: Annotated[GetRoomsListRequest, Depends()],
        interactor: FromDishka[GetRoomsUseCase]
) -> RoomsListResponse:
    return await interactor(rooms_request)


@router.get("/{id}/rooms/{room_id}", response_model=RoomResponse)
async def get_rooms_by_hotel_id_and_room_id(
        rooms_request: Annotated[GetRoomRequest, Depends()],
        interactor: FromDishka[GetRoomUseCase]
) -> RoomResponse:
    response = await interactor(rooms_request)
    if response is None:
        raise RoomNotFoundError
    return response


@router.post("/{id}/rooms/", response_model=RoomResponse)
async def create_room(
        id: int,
        #request: Request,
        #token_processor: FromDishka[JwtTokenProcessorImp],
        create_room_request: CreateRoomSchema,
        interactor: FromDishka[CreateRoomUseCase]
) -> RoomResponse:
    #if await token_processor.validate_token(request.scope["auth"]) is None:
    #    raise InvalidTokenError
    return await interactor(CreateRoomRequest(hotel_id=id, content=create_room_request))
