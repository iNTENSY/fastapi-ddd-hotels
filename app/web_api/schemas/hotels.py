from dataclasses import dataclass


@dataclass(frozen=True)
class UpdateHotelSchema:
    name: str
    location: str
    services: list[str]
    rooms_quantity: int
    image_id: int