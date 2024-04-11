from app.application.contracts.hotels.get_hotels_request import GetHotelListRequest, GetHotelRequest
from app.application.contracts.hotels.hotels_response import HotelsListResponse, HotelResponse
from app.application.protocols.interactor import Interactor
from app.domain.hotels.entity import Hotels
from app.domain.hotels.repository import IHotelRepository


class GetHotelsUseCase(Interactor[GetHotelListRequest, HotelsListResponse]):
    def __init__(self, hotels_repository: IHotelRepository) -> None:
        self._hotels_repository = hotels_repository

    async def __call__(self, request: GetHotelListRequest, **kwargs) -> HotelsListResponse:
        hotels: list[Hotels] = await self._hotels_repository.find_all(**request.model_dump())
        return HotelsListResponse(items=hotels,
                                  count=len(hotels))


class GetHotelUserCase(Interactor[GetHotelRequest, HotelResponse]):
    def __init__(self, hotels_repository: IHotelRepository) -> None:
        self._hotel_repository = hotels_repository

    async def __call__(self, request: GetHotelRequest, **kwargs) -> HotelResponse | None:
        hotel: list[Hotels] | None = await self._hotel_repository.filter_by(**request.model_dump())
        if not hotel:
            return None
        return await hotel[0].to_pydantic_model()
