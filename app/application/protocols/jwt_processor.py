from typing import Protocol, Optional

from app.domain.users.entity import UserId, UserEmail


class JwtTokenProcessor(Protocol):
    async def generate_token(self, user_id: UserId, user_email: UserEmail) -> str: ...

    async def validate_token(self, token: str) -> Optional[bool]: ...

    async def refresh_token(self, token: str) -> str: ...
