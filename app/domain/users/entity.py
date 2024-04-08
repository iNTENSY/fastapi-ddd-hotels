class User(Base):
    """Модель пользователей."""
    __tablename__ = "users"

    id: Mapped[intpk]
    email: Mapped[str]
    hashed_password: Mapped[str]
