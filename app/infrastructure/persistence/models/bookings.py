import datetime

from sqlalchemy import ForeignKey, Date, Computed
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.persistence.models.base import Base, uuidpk


class BookingsModel(Base):
    __tablename__ = "bookings"

    id: Mapped[uuidpk]

    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id", ondelete="CASCADE"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    date_from: Mapped[datetime.date] = mapped_column(Date)
    date_to: Mapped[datetime.date] = mapped_column(Date)
    price: Mapped[int]
    total_cost: Mapped[int] = mapped_column(Computed("(date_to - date_from) * price"))
    total_days: Mapped[int] = mapped_column(Computed("date_to - date_from"))
