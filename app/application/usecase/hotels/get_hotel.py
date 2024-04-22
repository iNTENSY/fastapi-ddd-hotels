from app.application.contracts.hotels.get_hotels_request import (
    GetHotelListRequest,
    GetHotelRequest,
)
from app.application.contracts.hotels.hotels_response import (
    HotelResponse,
    HotelsListResponse,
)
from app.application.protocols.interactor import Interactor
from app.domain.hotels.entity import Hotels
from app.domain.hotels.repository import IHotelRepository


class GetHotelsUseCase(Interactor[GetHotelListRequest, HotelsListResponse]):
    def __init__(self, hotels_repository: IHotelRepository) -> None:
        self.hotels_repository = hotels_repository

    async def __call__(self, request: GetHotelListRequest) -> HotelsListResponse:
        hotels: list[Hotels] = await self.hotels_repository.find_all(limit=request.limit, offset=request.offset)
        return await HotelsListResponse.create(hotels)


class GetHotelUseCase(Interactor[GetHotelRequest, HotelResponse]):
    def __init__(self, hotels_repository: IHotelRepository) -> None:
        self.hotel_repository = hotels_repository

    async def __call__(self, request: GetHotelRequest) -> HotelResponse | None:
        hotel = await self.hotel_repository.filter_by(id=request.id)
        if not hotel:
            return None
        return await HotelResponse.create(hotel[0])
