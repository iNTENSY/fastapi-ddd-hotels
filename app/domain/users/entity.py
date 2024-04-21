import uuid
from dataclasses import dataclass


@dataclass(frozen=True)
class UserId:
    value: uuid.UUID


@dataclass(frozen=True)
class UserEmail:
    value: str


@dataclass(frozen=True)
class UserHashedPassword:
    value: str


@dataclass
class Users:
    id: UserId
    email: UserEmail
    hashed_password: UserHashedPassword

    @staticmethod
    async def create(
            email: str,
            hashed_password: str
    ) -> "Users":
        return Users(
            id=UserId(value=uuid.uuid4()),
            email=UserEmail(value=email),
            hashed_password=UserHashedPassword(value=hashed_password)
        )

    async def raw(self) -> dict:
        return {key: value.value for key, value in vars(self).items()}