from dataclasses import dataclass


@dataclass(frozen=True)
class CreateRoomSchema:
    name: str
    description: str
    price: int
    services: list[str]
    quantity: int
    image_id: int