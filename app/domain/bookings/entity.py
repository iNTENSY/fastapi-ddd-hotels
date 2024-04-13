import datetime
from dataclasses import dataclass


@dataclass
class Bookings:
    id: int
    room_id: int
    user_id: int
    date_from: datetime.date
    date_to: datetime.date
    price: int
    total_cost: int
    total_days: int


    @property
    def total_days(self) -> int:
        return (self.date_to - self.date_from).days

    @property
    def total_cost(self) -> int:
        return (self.date_to - self.date_from).days * self.price
