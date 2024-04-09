from app.application.contracts.hotels.get_hotels_request import GetHotelRequest, GetHotelListRequest
from app.application.contracts.hotels.hotels_response import HotelsListResponse, HotelResponse
from app.infrastructure.persistance.repositories.hotel_repository import HotelRepositoryImp
from app.infrastructure.persistance.unitofwork import UnitOfWorkImp


class GetHotelsUseCase:
    def __init__(
            self,
            uow: UnitOfWorkImp,
            hotels_repository: HotelRepositoryImp
    ) -> None:
        self.__uow = uow
        self._hotels_repository = hotels_repository

    async def __call__(self, request: GetHotelListRequest) -> HotelsListResponse:
        # For test
        hotels = HotelsListResponse(
            items=[
                HotelResponse(id=i, name=str(i), location=str(i), services=[str(i)], rooms_quantity=i, image_id=i)
                for i in range(4)
            ],
            count=4
        )
        return hotels
