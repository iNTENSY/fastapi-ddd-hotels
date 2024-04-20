import uuid
from dataclasses import dataclass


@dataclass(frozen=True)
class RoomId:
    value: uuid.UUID


@dataclass(frozen=True)
class RoomHotelId:
    value: int


@dataclass(frozen=True)
class RoomName:
    value: str


@dataclass(frozen=True)
class RoomDescription:
    value: str


@dataclass(frozen=True)
class RoomPrice:
    value: int


@dataclass(frozen=True)
class RoomServices:
    value: list[str]


@dataclass(frozen=True)
class RoomQuantity:
    value: int


@dataclass
class Rooms:
    id: RoomId
    hotel_id: RoomHotelId
    name: RoomName
    description: RoomDescription
    price: RoomPrice
    services: RoomServices
    quantity: RoomQuantity
    image_id: int

    @staticmethod
    async def create(hotel_id: int,
                     name: str,
                     description: str,
                     price: int,
                     services: list[str],
                     quantity: int,
                     image_id: int) -> "Rooms":
        return Rooms(
            id=RoomId(value=uuid.uuid4()),
            hotel_id=RoomHotelId(hotel_id),
            name=RoomName(name),
            description=RoomDescription(description),
            price=RoomPrice(price),
            services=RoomServices(services),
            quantity=RoomQuantity(quantity),
            image_id=image_id
        )
