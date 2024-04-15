from dishka import Provider, Scope, provide

from app.application.protocols.jwt_processor import JwtTokenProcessor
from app.application.protocols.password_hasher import IPasswordHasher
from app.application.protocols.unitofwork import IUnitOfWork
from app.application.usecase.authentication.login import Login
from app.application.usecase.authentication.register import Register
from app.application.usecase.hotels.create_hotel import CreateHotelUseCase
from app.application.usecase.hotels.delete_hotel import DeleteHotelUseCase
from app.application.usecase.hotels.get_hotel import GetHotelsUseCase, GetHotelUserCase
from app.application.usecase.hotels.update_hotel import UpdateHotelUseCase
from app.domain.hotels.repository import IHotelRepository
from app.domain.users.repository import IUsersRepository
from app.infrastructure.authentication.jwt_processor import JoseJWTProcessor
from app.infrastructure.persistence.repositories.hotel_repository import HotelRepositoryImp
from app.infrastructure.persistence.repositories.users_repository import UsersRepositoryImp
from app.infrastructure.persistence.unitofwork import UnitOfWorkImp
from app.infrastructure.security.password_hasher import PasswordHasherImp


class UseCaseProvider(Provider):
    scope = Scope.REQUEST

    # Unit Of Work
    unit_of_work = provide(UnitOfWorkImp, provides=IUnitOfWork)

    # Repositories & password hasher & JWT
    hotels_repository = provide(HotelRepositoryImp, provides=IHotelRepository)
    users_repository = provide(UsersRepositoryImp, provides=IUsersRepository)
    password_hasher = provide(PasswordHasherImp, provides=IPasswordHasher)
    token_processor = provide(JoseJWTProcessor)

    # Use case
    get_hotels = provide(GetHotelsUseCase)
    get_hotel = provide(GetHotelUserCase)
    create_hotel = provide(CreateHotelUseCase)
    update_hotel = provide(UpdateHotelUseCase)
    delete_hotel = provide(DeleteHotelUseCase)

    auth_login = provide(Login)
    auth_register = provide(Register)
