from sqlalchemy.exc import IntegrityError

from app.application.contracts.hotels.hotels_response import HotelResponse
from app.application.contracts.hotels.update_hotels_request import UpdateHotelRequest
from app.application.protocols.interactor import Interactor
from app.application.protocols.unitofwork import IUnitOfWork
from app.domain.common.errors import UnprocessableEntityError
from app.domain.hotels.entity import Hotels
from app.domain.hotels.repository import IHotelRepository
from app.infrastructure.persistence.mappers.hotel_mapper import (
    hotel_from_dict_to_entity,
)


class UpdateHotelUseCase(Interactor[UpdateHotelRequest, HotelResponse]):
    def __init__(self, uow: IUnitOfWork, hotels_repository: IHotelRepository) -> None:
        self._uow = uow
        self._hotels_repository = hotels_repository

    async def __call__(self, request: UpdateHotelRequest) -> HotelResponse | None:
        data = {key: value for key, value in vars(request.content).items() if value}
        try:
            hotel = await self._hotels_repository.update(data=data, id=request.id)
            if not hotel:
                return None
            await self._uow.commit()
        except IntegrityError as exc:
            err_msg = str(exc.orig).split(":")[-1].replace("\n", "").strip()
            raise UnprocessableEntityError(err_msg)
        return await HotelResponse.create(hotel)
