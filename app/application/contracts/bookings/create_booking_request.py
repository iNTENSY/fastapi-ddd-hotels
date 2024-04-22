import uuid
from dataclasses import dataclass

from app.web_api.schemas.bookings import CreateBookingSchema


@dataclass(frozen=True)
class CreateBookingRequest:
    user_id: uuid.UUID
    content: CreateBookingSchema
