import uuid
from dataclasses import dataclass


@dataclass(frozen=True)
class DeleteHotelRequest:
    id: uuid.UUID
