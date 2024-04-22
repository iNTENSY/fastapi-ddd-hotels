import datetime
import uuid

from dataclasses import dataclass


@dataclass(frozen=True)
class CreateBookingSchema:
    room_id: uuid.UUID
    date_from: datetime.date
    date_to: datetime.date
