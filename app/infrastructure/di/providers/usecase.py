from dishka import Provider, Scope, provide

from app.application.protocols.jwt_processor import JwtTokenProcessor
from app.application.protocols.password_hasher import IPasswordHasher
from app.application.protocols.unitofwork import IUnitOfWork
from app.application.usecase.authentication.login import Login
from app.application.usecase.authentication.register import Register
from app.application.usecase.hotels.create_hotel import CreateHotelUseCase
from app.application.usecase.hotels.delete_hotel import DeleteHotelUseCase
from app.application.usecase.hotels.get_hotel import GetHotelsUseCase, GetHotelUseCase
from app.application.usecase.hotels.update_hotel import UpdateHotelUseCase
from app.application.usecase.rooms.create_room import CreateRoomUseCase
from app.application.usecase.rooms.delete_room import DeleteRoomUseCase
from app.application.usecase.rooms.get_room import GetRoomsUseCase, GetRoomUseCase
from app.application.usecase.rooms.update_room import UpdateRoomUseCase
from app.application.usecase.users.delete_user import DeleteUserUseCase
from app.application.usecase.users.get_user import GetUsersUseCase, GetUserUseCase
from app.domain.hotels.repository import IHotelRepository
from app.domain.rooms.repository import IRoomRepository
from app.domain.users.repository import IUserRepository
from app.infrastructure.authentication.jwt_processor import JwtTokenProcessorImp
from app.infrastructure.persistence.repositories.hotel_repository import (
    HotelRepositoryImp,
)
from app.infrastructure.persistence.repositories.room_repository import (
    RoomRepositoryImp,
)
from app.infrastructure.persistence.repositories.users_repository import (
    UsersRepositoryImp,
)
from app.infrastructure.persistence.unitofwork import UnitOfWorkImp
from app.infrastructure.security.password_hasher import PasswordHasherImp


class UseCaseProvider(Provider):
    scope = Scope.REQUEST

    # Unit Of Work
    unit_of_work = provide(UnitOfWorkImp, provides=IUnitOfWork)

    # Repositories & other
    hotels_repository = provide(HotelRepositoryImp, provides=IHotelRepository)
    users_repository = provide(UsersRepositoryImp, provides=IUserRepository)
    password_hasher = provide(PasswordHasherImp, provides=IPasswordHasher)
    room_repository = provide(RoomRepositoryImp, provides=IRoomRepository)
    token_processor = provide(JwtTokenProcessorImp, provides=JwtTokenProcessor)

    # Hotel use cases
    get_hotels = provide(GetHotelsUseCase)
    get_hotel = provide(GetHotelUseCase)
    create_hotel = provide(CreateHotelUseCase)
    update_hotel = provide(UpdateHotelUseCase)
    delete_hotel = provide(DeleteHotelUseCase)

    # Room use cases
    get_room = provide(GetRoomUseCase)
    get_rooms = provide(GetRoomsUseCase)
    create_room = provide(CreateRoomUseCase)
    update_room = provide(UpdateRoomUseCase)
    delete_room = provide(DeleteRoomUseCase)

    # Auth use cases
    auth_login = provide(Login)
    auth_register = provide(Register)

    # User use cases
    get_users = provide(GetUsersUseCase)
    get_user = provide(GetUserUseCase)
    delete_user = provide(DeleteUserUseCase)
