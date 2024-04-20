import bcrypt

from app.application.protocols.password_hasher import IPasswordHasher


class PasswordHasherImp(IPasswordHasher):
    @staticmethod
    async def hash_password(password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    @staticmethod
    async def verify_password(password: str, hashed_password: str) -> bool:
        try:
            result = bcrypt.checkpw(password.encode(), hashed_password.encode())
        except Exception as exc:
            return False
        return result
