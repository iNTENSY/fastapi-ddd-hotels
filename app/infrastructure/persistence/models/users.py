from sqlalchemy.orm import Mapped

from app.infrastructure.persistence.models.base import Base, intpk, uuidpk


class UsersModel(Base):
    """Модель пользователей."""
    __tablename__ = "users"

    id: Mapped[uuidpk]
    email: Mapped[str]
    hashed_password: Mapped[str]
