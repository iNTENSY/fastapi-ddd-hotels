from app.application.contracts.hotels.create_hotel_request import CreateHotelRequest
from app.application.contracts.hotels.hotels_response import HotelResponse
from app.application.protocols.interactor import Interactor
from app.application.protocols.unitofwork import IUnitOfWork
from app.domain.hotels.entity import Hotels
from app.domain.hotels.repository import IHotelRepository


class CreateHotelUseCase(Interactor[CreateHotelRequest, HotelResponse]):
    def __init__(self,
                 uow: IUnitOfWork,
                 hotels_repository: IHotelRepository) -> None:
        self._uow = uow
        self._hotels_repository = hotels_repository

    async def __call__(self, request: CreateHotelRequest, **kwargs) -> HotelResponse:
        hotel: Hotels = await self._hotels_repository.create(request.model_dump())
        await self._uow.commit()
        return await hotel.to_pydantic_model()
