from dishka import Provider, Scope, provide

from app.application.protocols.unitofwork import IUnitOfWork
from app.application.usecase.hotels.get_hotel import GetHotelsUseCase, GetHotelUserCase
from app.domain.hotels.repository import IHotelRepository
from app.infrastructure.persistence.repositories.hotel_repository import HotelRepositoryImp
from app.infrastructure.persistence.unitofwork import UnitOfWorkImp


class UseCaseProvider(Provider):
    scope = Scope.REQUEST

    # Unit Of Work
    unit_of_work = provide(UnitOfWorkImp, provides=IUnitOfWork)

    # Repositories
    hotels_repository = provide(HotelRepositoryImp, provides=IHotelRepository)

    # Use case
    get_hotels = provide(GetHotelsUseCase)
    get_hotel = provide(GetHotelUserCase)
