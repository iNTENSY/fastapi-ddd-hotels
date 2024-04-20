from pydantic import BaseModel, Field


class DeleteHotelRequest(BaseModel):
    hotel_id: int = Field(ge=0)
