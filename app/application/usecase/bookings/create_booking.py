from sqlalchemy.exc import IntegrityError

from app.application.contracts.bookings.booking_response import BookingResponse
from app.application.contracts.bookings.create_booking_request import (
    CreateBookingRequest,
)
from app.application.protocols.interactor import Interactor
from app.application.protocols.unitofwork import IUnitOfWork
from app.domain.bookings.entity import Bookings
from app.domain.bookings.errors import BookingAlreadyExistError
from app.domain.bookings.repository import IBookingRepository
from app.domain.common.errors import UnprocessableEntityError
from app.domain.rooms.repository import IRoomRepository


class CreateBookingUseCase(Interactor[CreateBookingRequest, BookingResponse]):
    def __init__(self, uow: IUnitOfWork, booking_repository: IBookingRepository, room_repository: IRoomRepository):
        self.__uow = uow
        self.booking_repository = booking_repository
        self.room_repository = room_repository

    async def __call__(self, request: CreateBookingRequest) -> BookingResponse | None:
        room = await self.room_repository.filter_by(id=request.content.room_id)
        booking = await Bookings.create(
            room_id=request.content.room_id,
            user_id=request.user_id,
            date_from=request.content.date_from,
            date_to=request.content.date_to,
            price=room[0].price.value,
        )
        try:
            if await self.booking_repository.is_exist(booking):
                raise BookingAlreadyExistError
            await self.booking_repository.create(booking)
            await self.__uow.commit()
        except IntegrityError as exc:
            err_msg = str(exc.orig).split(":")[-1].replace("\n", "").strip()
            raise UnprocessableEntityError(err_msg)
        return await BookingResponse.create(booking)
