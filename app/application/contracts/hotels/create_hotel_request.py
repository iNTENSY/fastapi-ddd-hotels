from pydantic import BaseModel


class CreateHotelRequest(BaseModel):
    name: str
    location: str
    services: list[str]
    rooms_quantity: int
    image_id: int

    class Config:
        from_attributes = True
