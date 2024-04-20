import datetime
from dataclasses import dataclass

from app.domain.common.errors import DomainValidationError
from app.domain.common.value_object import DomainValueObject


@dataclass(frozen=True)
class BookingRoomId(DomainValueObject):
    value: int

    def __post_init__(self) -> None:
        if not self.value:
            raise DomainValidationError("Room id is required.")


@dataclass
class Bookings:
    id: int
    room_id: int
    user_id: int
    date_from: datetime.date
    date_to: datetime.date
    price: int
    total_cost: int
    total_days: int


    @property
    def total_days(self) -> int:
        return (self.date_to - self.date_from).days

    @property
    def total_cost(self) -> int:
        return (self.date_to - self.date_from).days * self.price

    @staticmethod
    async def create(room_id, user_id, date_from, date_to) -> "Bookings":
        return Bookings(

        )