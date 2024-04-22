import datetime
import uuid
from dataclasses import dataclass

from app.domain.bookings.entity import Bookings


@dataclass(frozen=True)
class BookingResponse:
    id: uuid.UUID
    user_id: uuid.UUID
    room_id: uuid.UUID
    date_from: datetime.date
    date_to: datetime.date
    price: int
    total_cost: int
    total_days: int

    @staticmethod
    async def create(domain: Bookings) -> "BookingResponse":
        return BookingResponse(
            id=domain.id.value,
            user_id=domain.user_id.value,
            room_id=domain.room_id.value,
            date_from=domain.date_from.value,
            date_to=domain.date_to.value,
            price=domain.price.value,
            total_cost=domain.total_cost,
            total_days=domain.total_days,
        )
