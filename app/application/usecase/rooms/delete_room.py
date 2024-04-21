from app.application.contracts.rooms.delete_room_request import DeleteRoomRequest
from app.application.contracts.rooms.rooms_response import RoomResponse
from app.application.protocols.interactor import Interactor
from app.application.protocols.unitofwork import IUnitOfWork
from app.domain.rooms.repository import IRoomRepository


class DeleteRoomUseCase(Interactor[DeleteRoomRequest, RoomResponse]):
    def __init__(self, uow: IUnitOfWork, repository: IRoomRepository):
        self._uow = uow
        self._repository = repository

    async def __call__(self, request: DeleteRoomRequest) -> RoomResponse | None:
        room = await self._repository.delete(hotel_id=request.id, id=request.room_id)
        if not room:
            return None
        await self._uow.commit()
        return await RoomResponse.create(room)
