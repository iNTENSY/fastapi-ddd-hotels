from dishka import Provider, Scope, provide

from app.application.protocols.unitofwork import IUnitOfWork
from app.application.usecase.hotels.create_hotel import CreateHotelUseCase
from app.application.usecase.hotels.delete_hotel import DeleteHotelUseCase
from app.application.usecase.hotels.get_hotel import GetHotelsUseCase, GetHotelUserCase
from app.application.usecase.hotels.update_hotel import UpdateHotelUseCase
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
    create_hotel = provide(CreateHotelUseCase)
    update_hotel = provide(UpdateHotelUseCase)
    delete_hotel = provide(DeleteHotelUseCase)
