from sqladmin import ModelView

from app.infrastructure.persistence.models import BookingsModel


class BookingAdmin(ModelView, model=BookingsModel):
    column_list = [c.name for c in BookingsModel.__table__.c] # noqa