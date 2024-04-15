import datetime as dt

from typing import Protocol


class DateTimeProcessor(Protocol):
    async def get_current_time(self) -> dt.datetime: ...
