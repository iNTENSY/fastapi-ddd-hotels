from app.application.contracts.hotels.get_hotels_request import GetHotelRequest, GetHotelListRequest
from app.application.contracts.hotels.hotels_response import HotelsListResponse, HotelResponse
from app.application.protocols.unitofwork import IUnitOfWork
from app.domain.hotels.repository import IHotelRepository


class GetHotelsUseCase:
    def __init__(self) -> None:
        # self.__uow = uow
        pass

    async def __call__(self, request: GetHotelListRequest) -> HotelsListResponse:
        # hotels = await self.__mapper.find_all()
        hotels = HotelsListResponse(
            items=[
                HotelResponse(id=i, name=str(i), location=str(i), services=[str(i)], rooms_quantity=i, image_id=i)
                for i in range(4)
            ],
            count=4
        )
        return hotels
