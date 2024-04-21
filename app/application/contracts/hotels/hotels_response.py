import uuid
from dataclasses import dataclass

from pydantic import BaseModel

from app.domain.hotels.entity import Hotels


@dataclass(frozen=True)
class HotelResponse:
    id: uuid.UUID
    name: str
    location: str
    services: list[str]
    rooms_quantity: int
    image_id: int

    @staticmethod
    async def create(hotel: Hotels) -> "HotelResponse":
        return HotelResponse(
            id=hotel.id.value,
            name=hotel.name.value,
            location=hotel.location.value,
            services=hotel.services.value,
            rooms_quantity=hotel.rooms_quantity.value,
            image_id=hotel.image_id.value,
        )


@dataclass(frozen=True)
class HotelsListResponse:
    items: list[HotelResponse]
    count: int

    @staticmethod
    async def create(hotels: list[Hotels]) -> "HotelsListResponse":
        return HotelsListResponse(items=[await HotelResponse.create(hotel) for hotel in hotels], count=len(hotels))
