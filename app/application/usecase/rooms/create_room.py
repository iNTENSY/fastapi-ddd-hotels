from app.application.contracts.rooms.create_room_request import CreateRoomRequest
from app.application.contracts.rooms.rooms_response import RoomResponse
from app.application.protocols.interactor import Interactor
from app.application.protocols.unitofwork import IUnitOfWork
from app.domain.rooms.entity import Rooms
from app.domain.rooms.repository import IRoomRepository
from app.infrastructure.persistence.mappers.room_mapper import room_from_dataclass_to_dict


class CreateRoomUseCase(Interactor[CreateRoomRequest, RoomResponse]):
    def __init__(self, uow: IUnitOfWork, repository: IRoomRepository):
        self._uow = uow
        self._repository = repository

    async def __call__(self, request: CreateRoomRequest) -> RoomResponse:
        data = await room_from_dataclass_to_dict(request)
        room = await self._repository.create(data)
        await self._uow.commit()
        return await RoomResponse.create(room)
