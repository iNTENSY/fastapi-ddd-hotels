from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.persistence.models.base import Base, intpk


class HotelsModel(Base):
    __tablename__ = "hotels"

    id: Mapped[intpk]
    name: Mapped[str]
    location: Mapped[str]
    services: Mapped[list[str]] = mapped_column(JSON)
    rooms_quantity: Mapped[int]
    image_id: Mapped[int]

    UniqueConstraint("name", "location", name="unique_name_location")

    def __str__(self) -> str:
        return f"Отель {self.name}"
