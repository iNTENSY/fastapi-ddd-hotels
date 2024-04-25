from sqladmin import ModelView

from app.infrastructure.persistence.models import UsersModel


class UsersAdmin(ModelView, model=UsersModel):
    column_list = [UsersModel.id, UsersModel.email]
    column_details_exclude_list = [UsersModel.hashed_password]