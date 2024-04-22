from sqlalchemy.exc import IntegrityError

from app.application.contracts.rooms.rooms_response import RoomResponse
from app.application.contracts.rooms.update_hotel_request import UpdateRoomRequest
from app.application.protocols.interactor import Interactor
from app.application.protocols.unitofwork import IUnitOfWork
from app.domain.common.errors import UnprocessableEntityError
from app.domain.rooms.repository import IRoomRepository


class UpdateRoomUseCase(Interactor[UpdateRoomRequest, RoomResponse]):
    def __init__(self, uow: IUnitOfWork, room_repository: IRoomRepository):
        self.__uow = uow
        self.room_repository = room_repository

    async def __call__(self, request: UpdateRoomRequest) -> RoomResponse | None:
        data = {key: value for key, value in vars(request.content).items() if value}
        try:
            room = await self.room_repository.update(data=data, id=request.room_id)
            if not room:
                return None
            await self.__uow.commit()
        except IntegrityError as exc:
            err_msg = str(exc.orig).split(":")[-1].replace("\n", "").strip()
            raise UnprocessableEntityError(err_msg)
        return await RoomResponse.create(room)
