from app.application.contracts.rooms.delete_room_request import DeleteRoomRequest
from app.application.contracts.rooms.rooms_response import RoomResponse
from app.application.protocols.interactor import Interactor
from app.application.protocols.unitofwork import IUnitOfWork
from app.domain.rooms.repository import IRoomRepository


class DeleteRoomUseCase(Interactor[DeleteRoomRequest, RoomResponse]):
    def __init__(self, uow: IUnitOfWork, room_repository: IRoomRepository):
        self.__uow = uow
        self.room_repository = room_repository

    async def __call__(self, request: DeleteRoomRequest) -> RoomResponse | None:
        room = await self.room_repository.delete(hotel_id=request.id, id=request.room_id)
        if not room:
            return None
        await self.__uow.commit()
        return await RoomResponse.create(room)
