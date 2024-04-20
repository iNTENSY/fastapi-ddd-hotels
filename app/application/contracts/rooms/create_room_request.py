from dataclasses import dataclass

from app.web_api.schemas.rooms import CreateRoomSchema


@dataclass(frozen=True)
class CreateRoomRequest:
    hotel_id: int
    content: CreateRoomSchema
