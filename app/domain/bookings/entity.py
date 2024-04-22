import datetime
import uuid
from dataclasses import dataclass
from uuid import uuid4

from app.domain.common.errors import DomainValidationError
from app.domain.common.value_object import DomainValueObject


@dataclass(frozen=True)
class BookingId(DomainValueObject):
    value: uuid.UUID


@dataclass(frozen=True)
class BookingRoomId(DomainValueObject):
    value: uuid.UUID

    def __post_init__(self) -> None:
        if not self.value:
            raise DomainValidationError("Room id is required.")


@dataclass(frozen=True)
class BookingUserId(DomainValueObject):
    value: uuid.UUID


@dataclass(frozen=True)
class BookingDateFrom(DomainValueObject):
    value: datetime.date


@dataclass(frozen=True)
class BookingDateTo(DomainValueObject):
    value: datetime.date


@dataclass(frozen=True)
class BookingPrice(DomainValueObject):
    value: int


@dataclass
class Bookings:
    id: BookingId
    room_id: BookingRoomId
    user_id: BookingUserId
    date_from: BookingDateFrom
    date_to: BookingDateTo
    price: BookingPrice

    @property
    def total_days(self) -> int:
        return (self.date_to.value - self.date_from.value).days

    @property
    def total_cost(self) -> int:
        return (self.date_to.value - self.date_from.value).days * self.price.value

    @staticmethod
    async def create(
        room_id: uuid.UUID, user_id: uuid.UUID, date_from: datetime.date, date_to: datetime.date, price: int
    ) -> "Bookings":
        return Bookings(
            id=BookingId(value=uuid4()),
            room_id=BookingRoomId(value=room_id),
            user_id=BookingUserId(value=user_id),
            date_from=BookingDateFrom(value=date_from),
            date_to=BookingDateTo(value=date_to),
            price=BookingPrice(value=price),
        )

    async def raw(self) -> dict:
        return {key: value.value for key, value in vars(self).items()}
