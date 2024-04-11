from pydantic import BaseModel, Field


class DeleteHotelRequest(BaseModel):
    id: int = Field(ge=0)
