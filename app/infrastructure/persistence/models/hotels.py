from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.persistence.models.base import Base, intpk, uuidpk


class HotelsModel(Base):
    __tablename__ = "hotels"
    __table_args__ = (UniqueConstraint("name", "location", name="unique_name_location"),)

    id: Mapped[uuidpk]
    name: Mapped[str]
    location: Mapped[str]
    services: Mapped[list[str]] = mapped_column(JSON)
    rooms_quantity: Mapped[int]
    image_id: Mapped[int]

    def __str__(self) -> str:
        return f"Отель {self.name}"
