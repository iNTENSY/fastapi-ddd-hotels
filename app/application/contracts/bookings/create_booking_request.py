import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class CreateBookingRequest:
    room_id: int
    date_from: datetime.datetime
    date_to: datetime.datetime
