from app.application.contracts.rooms.get_rooms_request import (
    GetRoomRequest,
    GetRoomsListRequest,
)
from app.application.contracts.rooms.rooms_response import (
    RoomResponse,
    RoomsListResponse,
)
from app.application.protocols.interactor import Interactor
from app.domain.rooms.repository import IRoomRepository


class GetRoomUseCase(Interactor[GetRoomRequest, RoomResponse]):
    def __init__(self, repository: IRoomRepository):
        self._repository = repository

    async def __call__(self, request: GetRoomRequest) -> RoomResponse | None:
        room = await self._repository.filter_by(hotel_id=request.id, id=request.room_id)
        if not room:
            return None
        return await RoomResponse.create(room[0])


class GetRoomsUseCase(Interactor[GetRoomsListRequest, RoomsListResponse]):
    def __init__(self, repository: IRoomRepository):
        self._repository = repository

    async def __call__(self, request: GetRoomsListRequest) -> RoomsListResponse | None:
        rooms = await self._repository.find_all(hotel_id=request.id, limit=request.limit, offset=request.offset)
        return await RoomsListResponse.create(rooms)
