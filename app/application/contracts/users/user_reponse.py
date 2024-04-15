from dataclasses import dataclass

from app.domain.users.entity import Users


@dataclass(frozen=True)
class UserResponse:
    id: int
    email: str

    @staticmethod
    async def create(user: Users) -> "UserResponse":
        return UserResponse(
            id=user.id.value,
            email=user.email.value
        )



@dataclass(frozen=True)
class UserListResponse:
    items: list[UserResponse]
    count: int

    @staticmethod
    async def create(users: list[Users]) -> "UserListResponse":
        return UserListResponse(
            items=[await UserResponse.create(user) for user in users],
            count=len(users)
        )
