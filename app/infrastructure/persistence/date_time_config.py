import datetime as dt
from enum import Enum

from app.application.protocols.date_time import DateTimeProcessor


class Timezone(Enum):
    UTC = dt.timezone.utc
    GMT = dt.timezone(dt.timedelta(hours=0))
    CET = dt.timezone(dt.timedelta(hours=1))
    EET = dt.timezone(dt.timedelta(hours=2))
    MSK = dt.timezone(dt.timedelta(hours=3))
    IST = dt.timezone(dt.timedelta(hours=5, minutes=30))
    WIB = dt.timezone(dt.timedelta(hours=7))
    CST = dt.timezone(dt.timedelta(hours=8))
    JST = dt.timezone(dt.timedelta(hours=9))
    AEST = dt.timezone(dt.timedelta(hours=10))
    NZST = dt.timezone(dt.timedelta(hours=12))


class SystemDateTimeProvider(DateTimeProcessor):
    def __init__(self, tz: Timezone):
        self.tz = tz

    async def get_current_time(self) -> dt.datetime:
        return dt.datetime.now(tz=self.tz.value)
