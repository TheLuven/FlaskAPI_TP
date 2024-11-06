from typing import Optional

from pydantic import Field, BaseModel


class Imdb(BaseModel):
    rating: float = Field(...)
    votes: int = Field(...)
    id: int = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "rating": 8.7,
                "votes": 120000,
                "id": 123456
            }
        }

class ImdbUpdate(BaseModel):
    rating : Optional[float]
    votes : Optional[int]
    id : Optional[int]

    class Config:
        json_schema_extra = {
            "example": {
                "rating": 8.7,
                "votes": 120000,
                "id": 123456
            }
        }