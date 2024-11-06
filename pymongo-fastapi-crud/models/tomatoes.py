from datetime import datetime
from typing import Optional

from pydantic import Field, BaseModel

from models.review import Review


class Tomatoes(BaseModel):
    viewer: Review = Field(...)
    fresh: int = Field(...)
    critic: Review = Field(...)
    rotten: int = Field(...)
    lastupdated: datetime = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "viewer": {
                    "rating": 4.5,
                    "numReviews": 100,
                    "meter": 80
                },
                "fresh": 10,
                "critic": {
                    "rating": 4.5,
                    "numReviews": 100,
                    "meter": 80
                },
                "rotten": 10,
                "lastupdated": "2020-10-20 00:00:00"
            }
        }

class TomatoesUpdate(BaseModel):
    viewer : Optional[Review]
    fresh : Optional[int]
    critic : Optional[Review]
    rotten : Optional[int]
    lastupdated : Optional[datetime]

    class Config:
        json_schema_extra = {
            "example": {
                "viewer": {
                    "rating": 4.5,
                    "numReviews": 100,
                    "meter": 80
                },
                "fresh": 10,
                "critic": {
                    "rating": 4.5,
                    "numReviews": 100,
                    "meter": 80
                },
                "rotten": 10,
                "lastupdated": "2020-10-20 00:00:00"
            }
        }

