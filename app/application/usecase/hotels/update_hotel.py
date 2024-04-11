from app.application.contracts.hotels.hotels_response import HotelResponse
from app.application.contracts.hotels.update_hotels_request import UpdateHotelRequest
from app.application.protocols.interactor import Interactor
from app.application.protocols.unitofwork import IUnitOfWork
from app.domain.hotels.entity import Hotels
from app.domain.hotels.repository import IHotelRepository


class UpdateHotelUseCase(Interactor[UpdateHotelRequest, HotelResponse]):
    def __init__(self,
                 uow: IUnitOfWork,
                 hotels_repository: IHotelRepository) -> None:
        self._uow = uow
        self._hotels_repository = hotels_repository

    async def __call__(self, request: UpdateHotelRequest, **kwargs) -> HotelResponse | None:
        hotel: Hotels | None = await self._hotels_repository.update(data=request.model_dump(exclude_unset=True), id=kwargs.get("id"))
        if not hotel:
            return None
        return await hotel.to_pydantic_model()
