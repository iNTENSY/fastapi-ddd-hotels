import uuid
from dataclasses import dataclass

from app.domain.common.errors import DomainValidationError
from app.domain.common.value_object import DomainValueObject


@dataclass(frozen=True)
class HotelId(DomainValueObject):
    value: uuid.UUID


@dataclass(frozen=True)
class HotelName(DomainValueObject):
    value: str

    def __post_init__(self) -> None:
        if not self.value:
            raise DomainValidationError("Hotel name is required.")

        if len(self.value) > 100:
            raise DomainValidationError("Invalid hotel name. Hotel name must be less the 100 characters.")


@dataclass(frozen=True)
class HotelLocation(DomainValueObject):
    value: str

    def __post_init__(self) -> None:
        if not self.value:
            raise DomainValidationError("Hotel location is required.")


@dataclass(frozen=True)
class HotelServices(DomainValueObject):
    value: list[str]

    def __post_init__(self) -> None:
        if not self.value:
            raise DomainValidationError("Hotel services is required.")

        if not all(self.value):
            raise DomainValidationError("Hotel service has invalid data.")


@dataclass(frozen=True)
class HotelRoomQuantity(DomainValidationError):
    value: int

    def __post_init__(self) -> None:
        if not self.value:
            raise DomainValidationError("Provide the number of rooms in the hotel.")

        if self.value < 0:
            raise DomainValidationError("Rooms amount must be greater then 0")


@dataclass(frozen=True)
class HotelImageId(DomainValueObject):
    value: int


@dataclass
class Hotels:
    id: HotelId
    name: HotelName
    location: HotelLocation
    services: HotelServices
    rooms_quantity: HotelRoomQuantity
    image_id: HotelImageId

    @staticmethod
    async def create(name: str, location: str, services: list[str], rooms_quantity: int, image_id: int) -> "Hotels":
        return Hotels(
            id=HotelId(value=uuid.uuid4()),
            name=HotelName(value=name),
            location=HotelLocation(value=location),
            services=HotelServices(value=services),
            rooms_quantity=HotelRoomQuantity(value=rooms_quantity),
            image_id=HotelImageId(value=image_id),
        )

    async def raw(self) -> dict:
        return {key: value.value for key, value in vars(self).items()}
