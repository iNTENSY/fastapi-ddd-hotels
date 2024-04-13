from sqlalchemy.orm import Mapped

from app.infrastructure.persistence.models.base import Base, intpk


class UsersModel(Base):
    """Модель пользователей."""
    __tablename__ = "users"
    # __table_args__ = {'extend_existing': True}

    id: Mapped[intpk]
    email: Mapped[str]
    hashed_password: Mapped[str]
