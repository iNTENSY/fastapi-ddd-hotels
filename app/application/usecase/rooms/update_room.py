from app.application.contracts.rooms.rooms_response import RoomResponse
from app.application.contracts.rooms.update_hotel_request import UpdateRoomRequest
from app.application.protocols.interactor import Interactor
from app.application.protocols.unitofwork import IUnitOfWork
from app.domain.rooms.repository import IRoomRepository


class UpdateRoomUseCase(Interactor[UpdateRoomRequest, RoomResponse]):
    def __init__(self, uow: IUnitOfWork, repository: IRoomRepository):
        self._uow = uow
        self.repository = repository

    async def __call__(self, request: UpdateRoomRequest) -> RoomResponse: ...
