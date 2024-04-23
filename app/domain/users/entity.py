import uuid
from dataclasses import dataclass

from app.domain.common.entity import DomainEntity
from app.domain.common.value_object import DomainValueObject


@dataclass(frozen=True)
class UserId(DomainValueObject):
    value: uuid.UUID


@dataclass(frozen=True)
class UserEmail(DomainValueObject):
    value: str


@dataclass(frozen=True)
class UserHashedPassword(DomainValueObject):
    value: str


@dataclass
class Users(DomainEntity):
    id: UserId
    email: UserEmail
    hashed_password: UserHashedPassword

    @staticmethod
    async def create(email: str, hashed_password: str) -> "Users":
        return Users(
            id=UserId(value=uuid.uuid4()),
            email=UserEmail(value=email),
            hashed_password=UserHashedPassword(value=hashed_password),
        )

    async def raw(self) -> dict:
        return {key: value.value for key, value in vars(self).items()}
