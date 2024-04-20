import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class BookingResponse:
    id: int
    room_id: int
    date_from: datetime.datetime
    date_to: datetime.datetime
    price: int
    total_cost: int
    total_days: int
