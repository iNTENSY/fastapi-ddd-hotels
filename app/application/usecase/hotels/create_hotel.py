from sqlalchemy.exc import IntegrityError

from app.application.contracts.hotels.create_hotel_request import CreateHotelRequest
from app.application.contracts.hotels.hotels_response import HotelResponse
from app.application.protocols.interactor import Interactor
from app.application.protocols.unitofwork import IUnitOfWork
from app.domain.common.errors import UnprocessableEntityError
from app.domain.hotels.entity import Hotels
from app.domain.hotels.repository import IHotelRepository


class CreateHotelUseCase(Interactor[CreateHotelRequest, HotelResponse]):
    def __init__(self,
                 uow: IUnitOfWork,
                 hotels_repository: IHotelRepository) -> None:
        self._uow = uow
        self._hotels_repository = hotels_repository

    async def __call__(self, request: CreateHotelRequest) -> HotelResponse:
        hotel = await Hotels.create(name=request.name,
                                    location=request.location,
                                    services=request.services,
                                    rooms_quantity=request.rooms_quantity,
                                    image_id=request.image_id)
        try:
            await self._hotels_repository.create(hotel)
            await self._uow.commit()
        except IntegrityError as exc:
            err_msg = str(exc.orig).split(':')[-1].replace('\n', '').strip()
            raise UnprocessableEntityError(err_msg)

        return await HotelResponse.create(hotel)
