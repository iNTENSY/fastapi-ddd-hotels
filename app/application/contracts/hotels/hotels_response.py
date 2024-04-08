from pydantic import BaseModel


class HotelResponse(BaseModel):
    id: int
    name: str
    location: str
    services: list[str]
    rooms_quantity: int
    image_id: int


class HotelsListResponse(BaseModel):
    items: list[HotelResponse]
    count: int
