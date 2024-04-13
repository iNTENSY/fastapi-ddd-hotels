from pydantic import BaseModel

from app.domain.hotels.entity import Hotels


class HotelResponse(BaseModel):
    id: int
    name: str
    location: str
    services: list[str]
    rooms_quantity: int
    image_id: int

    class Config:
        from_attributes = True

    @classmethod
    async def create(cls, hotel: Hotels) -> "HotelResponse":
        return HotelResponse(
            id=hotel.id.value,
            name=hotel.name.value,
            location=hotel.location.value,
            services=hotel.services.value,
            rooms_quantity=hotel.rooms_quantity.value,
            image_id=hotel.image_id
        )


class HotelsListResponse(BaseModel):
    items: list[HotelResponse]
    count: int

    class Config:
        from_attributes = True
