from sqlalchemy import select, and_, or_
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.bookings.entity import Bookings
from app.domain.bookings.repository import IBookingRepository
from app.infrastructure.persistence.mappers.booking_mapper import booking_dict_to_entity
from app.infrastructure.persistence.models import BookingsModel


class BookingRepository(IBookingRepository):
    def __init__(self, connection: AsyncSession):
        self.__connection = connection

    async def filter_by(self, **parameters) -> list[Bookings] | None:
        statement = select(BookingsModel).filter_by(**parameters)
        result = await self.__connection.execute(statement)
        return [await booking_dict_to_entity(booking.__dict__) for booking in result]

    async def is_exist(self, domain: Bookings) -> bool:
        statement = select(BookingsModel).where(
            and_(
                BookingsModel.room_id == domain.room_id.value,
                or_(
                    and_(
                        BookingsModel.date_from >= domain.date_from.value,
                        BookingsModel.date_from <= domain.date_to.value,
                    ),
                    and_(
                        BookingsModel.date_from <= domain.date_from.value,
                        BookingsModel.date_to > domain.date_from.value,
                    ),
                ),
            )
        )
        result = (await self.__connection.execute(statement)).scalar_one_or_none()
        return True if result else False

    async def create(self, domain: Bookings) -> None:
        statement = insert(BookingsModel).values(await domain.raw())
        await self.__connection.execute(statement)
