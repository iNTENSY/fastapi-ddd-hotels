from typing import Protocol

from app.domain.hotels.entity import Hotels


class IHotelRepository(Protocol):
    async def create(self, hotel) -> Hotels: ...

    async def find_all(self, limit: int, offset: int) -> list[Hotels] | None: ...

    async def filter_by(self, **parameters) -> list[Hotels] | None: ...
