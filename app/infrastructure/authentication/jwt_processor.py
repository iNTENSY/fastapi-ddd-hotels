from datetime import timedelta
from typing import Optional

from jose import jwt, JWTError

from app.application.protocols.date_time import DateTimeProcessor
from app.application.protocols.jwt_processor import JwtTokenProcessor
from app.domain.users.entity import UserID, UserEmail, Users
from app.domain.users.errors import InvalidTokenError
from app.infrastructure.authentication.jwt_settings import JWTSettings


class JoseJWTProcessor(JwtTokenProcessor):
    def __init__(self, jwt_options: JWTSettings, date_time_provider: DateTimeProcessor):
        self._jwt_options = jwt_options
        self.date_time_provider = date_time_provider

    async def generate_token(self, user_id: UserID, user_email: UserEmail) -> str:
        issued_at = await self.date_time_provider.get_current_time()
        expiration_time = issued_at + timedelta(minutes=self._jwt_options.expires_in)

        payload = {
            "iat": issued_at,
            "exp": expiration_time,
            "sub": str(user_id.value),
            "email": user_email.value
        }

        encoded_jwt = jwt.encode(payload, self._jwt_options.secret, self._jwt_options.algorithm)
        return encoded_jwt

    async def validate_token(self, token: str) -> tuple[UserID, UserEmail] | None:
        try:
            payload = jwt.decode(token, self._jwt_options.secret, self._jwt_options.algorithm)
            return UserID(payload["sub"]), UserEmail(payload["email"])
        except (JWTError, ValueError, KeyError):
            return None

    async def refresh_token(self, token: str) -> str:
        payload = await self.validate_token(token)
        if payload is None:
            raise InvalidTokenError
        return await self.generate_token(user_id=payload[0], user_email=payload[1])
