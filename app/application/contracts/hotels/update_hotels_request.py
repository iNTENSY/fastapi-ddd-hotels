from pydantic import BaseModel


class UpdateHotelRequest(BaseModel):
    name: str | None = None
    location: str | None = None
    services: list[str] | None = []
    rooms_quantity: int | None = None
    image_id: int | None = None

    class Config:
        from_attributes = True
