from dataclasses import dataclass

from app.domain.rooms.entity import Rooms


@dataclass(frozen=True)
class RoomResponse:
    id: int
    hotel_id: int
    name: str
    description: str
    price: int
    services: list[str]
    quantity: int
    image_id: int

    @staticmethod
    async def create(room: Rooms) -> "RoomResponse":
        return RoomResponse(
            id=room.id,
            hotel_id=room.hotel_id,
            name=room.name,
            description=room.description,
            price=room.price,
            services=room.services,
            quantity=room.quantity,
            image_id=room.image_id,
        )


@dataclass(frozen=True)
class RoomsListResponse:
    items: list[RoomResponse]
    count: int

    @staticmethod
    async def create(rooms: list[Rooms]) -> "RoomsListResponse":
        return RoomsListResponse(
            items=[await RoomResponse.create(room) for room in rooms],
            count=len(rooms)
        )
