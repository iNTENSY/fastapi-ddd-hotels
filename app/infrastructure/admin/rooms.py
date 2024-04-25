from sqladmin import ModelView

from app.infrastructure.persistence.models import RoomsModel


class RoomsAdmin(ModelView, model=RoomsModel):
    column_list = [c.name for c in RoomsModel.__table__.c] # noqa