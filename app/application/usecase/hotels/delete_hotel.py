from app.application.contracts.hotels.delete_hotels_request import DeleteHotelRequest
from app.application.contracts.hotels.hotels_response import HotelResponse
from app.application.protocols.interactor import Interactor
from app.application.protocols.unitofwork import IUnitOfWork
from app.domain.hotels.entity import Hotels
from app.domain.hotels.repository import IHotelRepository


class DeleteHotelUseCase(Interactor[DeleteHotelRequest, HotelResponse]):
    def __init__(self,
                 uow: IUnitOfWork,
                 hotels_repository: IHotelRepository) -> None:
        self._uow = uow
        self._hotels_repository = hotels_repository

    async def __call__(self, request: DeleteHotelRequest, **kwargs) -> HotelResponse | None:
        hotel: Hotels = await self._hotels_repository.delete(id=request.id)
        if not hotel:
            return None
        await self._uow.commit()
        return await HotelResponse.create(hotel)
