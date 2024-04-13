from dataclasses import dataclass


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
