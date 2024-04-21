import uuid
from dataclasses import dataclass

from app.domain.rooms.entity import Rooms


@dataclass(frozen=True)
class RoomResponse:
    id: uuid.UUID
    hotel_id: uuid.UUID
    name: str
    description: str
    price: int
    services: list[str]
    quantity: int
    image_id: int

    @staticmethod
    async def create(room: Rooms) -> "RoomResponse":
        return RoomResponse(
            id=room.id.value,
            hotel_id=room.hotel_id.value,
            name=room.name.value,
            description=room.description.value,
            price=room.price.value,
            services=room.services.value,
            quantity=room.quantity.value,
            image_id=room.image_id.value,
        )


@dataclass(frozen=True)
class RoomsListResponse:
    items: list[RoomResponse]
    count: int

    @staticmethod
    async def create(rooms: list[Rooms]) -> "RoomsListResponse":
        return RoomsListResponse(items=[await RoomResponse.create(room) for room in rooms], count=len(rooms))
