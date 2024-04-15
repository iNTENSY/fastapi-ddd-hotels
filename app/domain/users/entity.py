from dataclasses import dataclass


@dataclass(frozen=True)
class UserID:
    value: int


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
            id: int,
            email: str,
            hashed_password: str
    ) -> "Users":
        return Users(
            id=UserID(value=id),
            email=UserEmail(value=email),
            hashed_password=hashed_password
        )
