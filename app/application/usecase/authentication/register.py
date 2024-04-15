from app.application.contracts.authentication.authentication_response import AuthResponse
from app.application.contracts.authentication.register_request import RegisterRequest
from app.application.protocols.interactor import Interactor
from app.application.protocols.password_hasher import IPasswordHasher
from app.application.protocols.unitofwork import IUnitOfWork
from app.domain.users.repository import IUserRepository


class Register(Interactor[RegisterRequest, AuthResponse]):
    def __init__(self,
                 uow: IUnitOfWork,
                 users_repository: IUserRepository,
                 password_hasher: IPasswordHasher) -> None:
        self._uow = uow
        self.users_repository = users_repository
        self.password_hasher = password_hasher

    async def __call__(self, request: RegisterRequest) -> AuthResponse | None:
        hashed_password = await self.password_hasher.hash_password(request.password)
        user = await self.users_repository.create({"email": request.email, "hashed_password": hashed_password})
        await self._uow.commit()
        return AuthResponse(id=user.id.value, email=user.email.value)
