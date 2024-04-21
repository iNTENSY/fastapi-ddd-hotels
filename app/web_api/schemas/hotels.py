from dataclasses import dataclass, field


@dataclass(frozen=True)
class UpdateHotelSchema:
    name: str | None = None
    location: str | None = None
    services: list[str] | None = field(default_factory=list)
    rooms_quantity: int | None = None
    image_id: int | None = None
