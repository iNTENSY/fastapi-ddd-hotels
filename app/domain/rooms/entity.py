from dataclasses import dataclass


@dataclass(frozen=True)
class RoomId:
    value: int


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
    id: int
    hotel_id: int
    name: str
    description: str
    price: int
    services: list[str]
    quantity: int
    image_id: int

    @staticmethod
    async def create(id: int,
                     hotel_id: int,
                     name: str,
                     description: str,
                     price: int,
                     services: list[str],
                     quantity: int,
                     image_id: int) -> "Rooms":
        return Rooms(
            id=RoomId(id).value,
            hotel_id=RoomHotelId(hotel_id).value,
            name=RoomName(name).value,
            description=RoomDescription(description).value,
            price=RoomPrice(price).value,
            services=RoomServices(services).value,
            quantity=RoomQuantity(quantity).value,
            image_id=image_id
        )
