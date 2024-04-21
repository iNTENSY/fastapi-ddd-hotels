from dataclasses import dataclass


@dataclass(frozen=True)
class CreateRoomSchema:
    name: str
    description: str
    price: int
    services: list[str]
    quantity: int
    image_id: int


@dataclass(frozen=True)
class UpdateRoomSchema:
    name: str | None = None
    description: str | None = None
    price: int | None = None
    services: list[str] | None = None
    quantity: int | None = None
    image_id: int | None = None
