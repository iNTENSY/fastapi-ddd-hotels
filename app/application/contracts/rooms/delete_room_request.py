import uuid
from dataclasses import dataclass


@dataclass(frozen=True)
class DeleteRoomRequest:
    id: uuid.UUID
    room_id: uuid.UUID
