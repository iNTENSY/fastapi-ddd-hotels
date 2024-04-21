import uuid
from dataclasses import dataclass

from app.web_api.schemas.hotels import UpdateHotelSchema


@dataclass(frozen=True)
class UpdateHotelRequest:
    id: uuid.UUID
    content: UpdateHotelSchema
