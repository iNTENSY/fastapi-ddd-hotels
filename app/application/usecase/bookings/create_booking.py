from app.application.contracts.bookings.booking_response import BookingResponse
from app.application.contracts.bookings.create_booking_request import CreateBookingRequest
from app.application.protocols.interactor import Interactor
from app.application.protocols.unitofwork import IUnitOfWork
from app.domain.bookings.repository import IBookingRepository
from app.domain.rooms.entity import Rooms


class CreateBookingUseCase(Interactor[CreateBookingRequest, BookingResponse]):
    def __init__(self, uow: IUnitOfWork, booking_repository: IBookingRepository):
        self._uow = uow
        self._booking_repository = booking_repository

    async def __call__(self, request: CreateBookingRequest) -> BookingResponse | None:
        # -------------
        #
        # Проверить существование
        #
        # -------------
        ...