from typing import Protocol, Optional


class JwtTokenProcessor(Protocol):
    def generate_token(self, user_id) -> str: ...

    def validate_token(self, token: str) -> Optional[bool]: ...
