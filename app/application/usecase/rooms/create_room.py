from sqlalchemy.exc import IntegrityError

from app.application.contracts.rooms.create_room_request import CreateRoomRequest
from app.application.contracts.rooms.rooms_response import RoomResponse
from app.application.protocols.interactor import Interactor
from app.application.protocols.unitofwork import IUnitOfWork
from app.domain.common.errors import UnprocessableEntityError
from app.domain.rooms.entity import Rooms
from app.domain.rooms.repository import IRoomRepository
from app.infrastructure.persistence.mappers.room_mapper import room_from_dataclass_to_dict


class CreateRoomUseCase(Interactor[CreateRoomRequest, RoomResponse]):
    def __init__(self, uow: IUnitOfWork, repository: IRoomRepository):
        self._uow = uow
        self._repository = repository

    async def __call__(self, request: CreateRoomRequest) -> RoomResponse:
        room = await Rooms.create(
            hotel_id=request.hotel_id,
            name=request.content.name,
            description=request.content.description,
            price=request.content.price,
            services=request.content.services,
            quantity=request.content.quantity,
            image_id=request.content.image_id
        )
        try:
            await self._repository.create(room)
            await self._uow.commit()
        except IntegrityError as exc:
            err_msg = str(exc.orig).split(':')[-1].replace('\n', '').strip()
            raise UnprocessableEntityError(err_msg)
        return await RoomResponse.create(room)
