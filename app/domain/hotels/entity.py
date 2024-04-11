from typing import TYPE_CHECKING

from sqlalchemy import JSON, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.application.contracts.hotels.hotels_response import HotelResponse
from app.domain.common.entity import DomainModel, DomainModelID


if TYPE_CHECKING:
    from app.domain.rooms.entity import Rooms


class Hotels(DomainModel):
    __tablename__ = "hotels"

    id: Mapped[DomainModelID]
    name: Mapped[str]
    location: Mapped[str]
    services: Mapped[list[str]] = mapped_column(JSON)
    rooms_quantity: Mapped[int]
    image_id: Mapped[int]

    #rooms = relationship("Rooms", back_populates="hotel", lazy="dynamic")
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
