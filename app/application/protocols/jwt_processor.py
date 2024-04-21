from typing import Optional, Protocol

from app.domain.users.entity import UserEmail, UserId


class JwtTokenProcessor(Protocol):
    async def generate_token(self, user_id: UserId, user_email: UserEmail) -> str: ...

    async def validate_token(self, token: str) -> bool | None: ...

    async def refresh_token(self, token: str) -> str: ...
