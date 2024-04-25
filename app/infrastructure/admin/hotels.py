from sqladmin import ModelView

from app.infrastructure.persistence.models import HotelsModel


class HotelAdmin(ModelView, model=HotelsModel):
    column_list = [c.name for c in HotelsModel.__table__.c] # noqa
