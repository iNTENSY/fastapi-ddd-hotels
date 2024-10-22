import uuid
from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute, inject
from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from starlette.requests import Request

from app.application.contracts.hotels.create_hotel_request import CreateHotelRequest
from app.application.contracts.hotels.delete_hotels_request import DeleteHotelRequest
from app.application.contracts.hotels.get_hotels_request import (
    GetHotelListRequest,
    GetHotelRequest,
)
from app.application.contracts.hotels.hotels_response import (
    HotelResponse,
    HotelsListResponse,
)
from app.application.contracts.hotels.update_hotels_request import UpdateHotelRequest
from app.application.contracts.rooms.create_room_request import CreateRoomRequest
from app.application.contracts.rooms.delete_room_request import DeleteRoomRequest
from app.application.contracts.rooms.get_rooms_request import (
    GetRoomRequest,
    GetRoomsListRequest,
)
from app.application.contracts.rooms.rooms_response import (
    RoomResponse,
    RoomsListResponse,
)
from app.application.contracts.rooms.update_hotel_request import UpdateRoomRequest
from app.application.protocols.jwt_processor import JwtTokenProcessor
from app.application.usecase.hotels.create_hotel import CreateHotelUseCase
from app.application.usecase.hotels.delete_hotel import DeleteHotelUseCase
from app.application.usecase.hotels.get_hotel import GetHotelsUseCase, GetHotelUseCase
from app.application.usecase.hotels.update_hotel import UpdateHotelUseCase
from app.application.usecase.rooms.create_room import CreateRoomUseCase
from app.application.usecase.rooms.delete_room import DeleteRoomUseCase
from app.application.usecase.rooms.get_room import GetRoomsUseCase, GetRoomUseCase
from app.application.usecase.rooms.update_room import UpdateRoomUseCase
from app.domain.hotels.errors import HotelNotFoundError
from app.domain.rooms.errors import RoomNotFoundError
from app.domain.users.errors import InvalidTokenError
from app.infrastructure.authentication.permissions import auth_required
from app.web_api.schemas.hotels import UpdateHotelSchema
from app.web_api.schemas.rooms import CreateRoomSchema, UpdateRoomSchema

router = APIRouter(prefix="/hotels", tags=["Hotels"], route_class=DishkaRoute)


@router.get(path="/", response_model=HotelsListResponse, dependencies=[Depends(auth_required)])
# @cache(expire=60 * 10)
@inject
async def get_hotels(
    request: Request,
    get_hotels_request: Annotated[GetHotelListRequest, Depends()],
    interactor: FromDishka[GetHotelsUseCase],
    token_processor: FromDishka[JwtTokenProcessor],
) -> HotelsListResponse:
    if await token_processor.validate_token(request.scope["auth"]) is None:
        raise InvalidTokenError
    return await interactor(get_hotels_request)


@router.get(path="/{id}", response_model=HotelResponse)
# @cache(expire=60 * 5)
@inject
async def get_hotel(
    get_hotel_request: Annotated[GetHotelRequest, Depends()],
    interactor: FromDishka[GetHotelUseCase],
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
    token_processor: FromDishka[JwtTokenProcessor],
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
    token_processor: FromDishka[JwtTokenProcessor],
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
    id: uuid.UUID,
    request: Request,
    update_hotel_schema: UpdateHotelSchema,
    update_hotel_interactor: FromDishka[UpdateHotelUseCase],
    token_processor: FromDishka[JwtTokenProcessor],
) -> HotelResponse:
    if await token_processor.validate_token(request.scope["auth"]) is None:
        raise InvalidTokenError
    response = await update_hotel_interactor(UpdateHotelRequest(id=id, content=update_hotel_schema))
    if response is None:
        raise HotelNotFoundError
    return response


@router.get("/{id}/rooms", response_model=RoomsListResponse)
async def get_rooms_by_hotel_id(
    rooms_request: Annotated[GetRoomsListRequest, Depends()], interactor: FromDishka[GetRoomsUseCase]
) -> RoomsListResponse:
    return await interactor(rooms_request)


@router.get("/{id}/rooms/{room_id}", response_model=RoomResponse)
async def get_rooms_by_hotel_id_and_room_id(
    rooms_request: Annotated[GetRoomRequest, Depends()], interactor: FromDishka[GetRoomUseCase]
) -> RoomResponse:
    response = await interactor(rooms_request)
    if response is None:
        raise RoomNotFoundError
    return response


@router.post("/{id}/rooms/", response_model=RoomResponse, dependencies=[Depends(auth_required)])
async def create_room(
    id: uuid.UUID,
    request: Request,
    token_processor: FromDishka[JwtTokenProcessor],
    create_room_schema: CreateRoomSchema,
    interactor: FromDishka[CreateRoomUseCase],
) -> RoomResponse:
    if await token_processor.validate_token(request.scope["auth"]) is None:
        raise InvalidTokenError
    return await interactor(CreateRoomRequest(hotel_id=id, content=create_room_schema))


@router.patch("/{id}/rooms/{room_id}", response_model=RoomResponse, dependencies=[Depends(auth_required)])
async def update_room(
    id: uuid.UUID,
    room_id: uuid.UUID,
    request: Request,
    token_processor: FromDishka[JwtTokenProcessor],
    update_room_schema: UpdateRoomSchema,
    interactor: FromDishka[UpdateRoomUseCase],
) -> RoomResponse:
    if await token_processor.validate_token(request.scope["auth"]) is None:
        raise InvalidTokenError
    response = await interactor(UpdateRoomRequest(id=id, content=update_room_schema, room_id=room_id))
    if response is None:
        raise RoomNotFoundError
    return response


@router.delete("/{id}/rooms/{room_id}", response_model=RoomResponse, dependencies=[Depends(auth_required)])
async def delete_room(
    delete_room_request: Annotated[DeleteRoomRequest, Depends()],
    request: Request,
    token_processor: FromDishka[JwtTokenProcessor],
    interactor: FromDishka[DeleteRoomUseCase],
) -> RoomResponse:
    if await token_processor.validate_token(request.scope["auth"]) is None:
        raise InvalidTokenError
    response = await interactor(delete_room_request)
    if response is None:
        raise RoomNotFoundError
    return response
