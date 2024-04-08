from typing import Protocol


class IHotelRepository(Protocol):
    async def create(self, hotel):
        ...

    async def find_all(self):
        ...