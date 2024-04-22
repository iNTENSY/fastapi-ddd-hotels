import uuid
from dataclasses import dataclass

from app.domain.common.value_object import DomainValueObject


@dataclass(frozen=True)
class RoomId(DomainValueObject):
    value: uuid.UUID


@dataclass(frozen=True)
class RoomHotelId(DomainValueObject):
    value: uuid.UUID


@dataclass(frozen=True)
class RoomName(DomainValueObject):
    value: str


@dataclass(frozen=True)
class RoomDescription(DomainValueObject):
    value: str


@dataclass(frozen=True)
class RoomPrice(DomainValueObject):
    value: int


@dataclass(frozen=True)
class RoomServices(DomainValueObject):
    value: list[str]


@dataclass(frozen=True)
class RoomQuantity(DomainValueObject):
    value: int


@dataclass(frozen=True)
class RoomImageId(DomainValueObject):
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
    image_id: RoomImageId

    @staticmethod
    async def create(
        hotel_id: uuid.UUID, name: str, description: str, price: int, services: list[str], quantity: int, image_id: int
    ) -> "Rooms":
        return Rooms(
            id=RoomId(value=uuid.uuid4()),
            hotel_id=RoomHotelId(hotel_id),
            name=RoomName(name),
            description=RoomDescription(description),
            price=RoomPrice(price),
            services=RoomServices(services),
            quantity=RoomQuantity(quantity),
            image_id=RoomImageId(image_id),
        )

    async def raw(self) -> dict:
        return {key: value.value for key, value in vars(self).items()}
