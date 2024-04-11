from typing import Optional

from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.domain.common.entity import DomainModel, DomainModelID

from app.domain.hotels.entity import Hotels
from app.domain.bookings.entity import Bookings


class Rooms(DomainModel):
    __tablename__ = "rooms"

    id: Mapped[DomainModelID]

    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id", ondelete="CASCADE"))
    hotel: Mapped["Hotels"] = relationship(back_populates="rooms")

    name: Mapped[str]
    description: Mapped[Optional[str]]
    price: Mapped[int]
    services: Mapped[list[str]] = mapped_column(JSON)
    quantity: Mapped[int]
    image_id: Mapped[int]

    bookings: Mapped[list["Bookings"]] = relationship(back_populates="room")
