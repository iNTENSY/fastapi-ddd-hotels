from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.persistence.models.base import Base, intpk, uuidpk


class UsersModel(Base):
    """Модель пользователей."""

    __tablename__ = "users"

    id: Mapped[uuidpk]
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
