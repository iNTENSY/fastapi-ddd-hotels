from sqlalchemy.orm import Mapped

from app.domain.common.entity import DomainModel, DomainModelID


class Users(DomainModel):
    """Модель пользователей."""
    __tablename__ = "users"

    id: Mapped[DomainModelID]
    email: Mapped[str]
    hashed_password: Mapped[str]
