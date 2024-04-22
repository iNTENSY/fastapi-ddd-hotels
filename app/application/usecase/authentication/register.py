from app.application.contracts.authentication.authentication_response import (
    AuthResponse,
)
from app.application.contracts.authentication.register_request import RegisterRequest
from app.application.protocols.interactor import Interactor
from app.application.protocols.password_hasher import IPasswordHasher
from app.application.protocols.unitofwork import IUnitOfWork
from app.domain.users.entity import Users
from app.domain.users.repository import IUserRepository


class Register(Interactor[RegisterRequest, AuthResponse]):
    def __init__(self, uow: IUnitOfWork, user_repository: IUserRepository, password_hasher: IPasswordHasher) -> None:
        self.__uow = uow
        self.user_repository = user_repository
        self.password_hasher = password_hasher

    async def __call__(self, request: RegisterRequest) -> AuthResponse | None:
        hashed_password = await self.password_hasher.hash_password(request.password)
        user = await Users.create(request.email, hashed_password)
        await self.user_repository.create(user)
        await self.__uow.commit()
        return AuthResponse(id=user.id.value, email=user.email.value)
