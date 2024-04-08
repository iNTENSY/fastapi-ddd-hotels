from pydantic import BaseModel, Field


class GetHotelListRequest(BaseModel):
    limit: int = Field(default=20, ge=0)
    offset: int = Field(default=0, ge=0)

class GetHotelRequest(BaseModel):
    id: int = Field(ge=0)
