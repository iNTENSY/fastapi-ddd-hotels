import uuid
from dataclasses import dataclass

from app.web_api.schemas.rooms import UpdateRoomSchema


@dataclass(frozen=True)
class UpdateRoomRequest:
    id: uuid.UUID
    content: UpdateRoomSchema
