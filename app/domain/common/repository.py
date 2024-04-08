from typing import Protocol


class IHotelRepository(Protocol):
    async def create(self, hotel):
        raise NotImplementedError

    async def find_all(self):
        raise NotImplementedError