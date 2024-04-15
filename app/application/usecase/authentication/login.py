from app.application.contracts.authentication.authentication_response import AuthResponse
from app.application.contracts.authentication.login_request import LoginRequest
from app.application.protocols.interactor import Interactor
from app.application.protocols.password_hasher import IPasswordHasher
from app.domain.users.errors import UserNotFoundError, InvalidUserDataError
from app.domain.users.repository import IUserRepository


class Login(Interactor[LoginRequest, AuthResponse]):
    def __init__(self, users_repository: IUserRepository, password_hasher: IPasswordHasher):
        self.users_repository = users_repository
        self.password_hasher = password_hasher

    async def __call__(self, request: LoginRequest) -> AuthResponse | None:
        user = await self.users_repository.filter_by(email=request.email)
        if not user:
            raise UserNotFoundError
        if not await self.password_hasher.verify_password(request.password,
                                                          user[0].hashed_password):
            raise InvalidUserDataError
        return AuthResponse(id=user[0].id.value, email=user[0].email.value)
