from sqlalchemy import JSON, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.application.contracts.hotels.hotels_response import HotelResponse
from app.domain.common.entity import DomainModel, DomainModelID


class Hotels(DomainModel):
    __tablename__ = "hotels"

    id: Mapped[DomainModelID]
    name: Mapped[str]
    location: Mapped[str]
    services: Mapped[list[str]] = mapped_column(JSON)
    rooms_quantity: Mapped[int]
    image_id: Mapped[int]

    UniqueConstraint("name", "location", name="unique_name_location")

    def __str__(self) -> str:
        return f"Отель {self.name}"

    async def to_pydantic_model(self) -> HotelResponse:
        return HotelResponse(
            id=self.id,
            name=self.name,
            location=self.location,
            services=self.services,
            rooms_quantity=self.rooms_quantity,
            image_id=self.image_id
        )
