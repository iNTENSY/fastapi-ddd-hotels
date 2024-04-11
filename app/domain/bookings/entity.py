import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Date, Computed, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.domain.common.entity import DomainModel, DomainModelID

from app.domain.rooms.entity import Rooms
from app.domain.users.entity import Users


class Bookings(DomainModel):
    __tablename__ = "bookings"

    id: Mapped[DomainModelID]

    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id", ondelete="CASCADE"))
    room: Mapped["Rooms"] = relationship(back_populates="bookings")

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    user: Mapped["Users"] = relationship(back_populates="bookings")

    date_from: Mapped[datetime.date] = mapped_column(Date)
    date_to: Mapped[datetime.date] = mapped_column(Date)
    price: Mapped[int]
    total_cost: Mapped[int] = mapped_column(Computed("(date_to - date_from) * price"))
    total_days: Mapped[int] = mapped_column(Computed("date_to - date_from"))
