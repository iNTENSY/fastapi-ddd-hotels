import uuid
from dataclasses import dataclass


@dataclass(frozen=True)
class UserID:
    value: uuid.UUID


@dataclass(frozen=True)
class UserEmail:
    value: str


@dataclass
class Users:
    id: UserID
    email: UserEmail
    hashed_password: str

    @staticmethod
    async def create(
            email: str,
            hashed_password: str
    ) -> "Users":
        return Users(
            id=UserID(value=uuid.uuid4()),
            email=UserEmail(value=email),
            hashed_password=hashed_password
        )
