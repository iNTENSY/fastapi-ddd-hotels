import uuid
from dataclasses import dataclass, field


@dataclass(frozen=True)
class GetRoomsListRequest:
    id: uuid.UUID
    limit: int = field(default=20)
    offset: int = field(default=0)


@dataclass(frozen=True)
class GetRoomRequest:
    id: int = field(default=0)
    room_id: int = field(default=0)
