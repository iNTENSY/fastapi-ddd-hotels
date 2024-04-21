from typing import Optional

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.persistence.models.base import Base, intpk, uuidpk


class RoomsModel(Base):
    __tablename__ = "rooms"
    __table_args__ = (UniqueConstraint("name", "hotel_id", name="unique_room_hotel_id"),)

    id: Mapped[uuidpk]
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id", ondelete="CASCADE"))

    name: Mapped[str]
    description: Mapped[Optional[str]]
    price: Mapped[int]
    services: Mapped[list[str]] = mapped_column(JSON)
    quantity: Mapped[int]
    image_id: Mapped[int]
