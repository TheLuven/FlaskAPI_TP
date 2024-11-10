from datetime import datetime
from typing import Optional

from pydantic import Field, BaseModel

from models.mongo.review import Review


class Tomatoes(BaseModel):
    viewer: Review = Field(...)
    fresh: Optional[int] = None
    critic: Optional[Review] = None
    rotten: Optional[int] = None
    dvd: Optional[datetime] = None
    website: Optional[str] = None
    production: Optional[str] = None
    lastupdated: Optional[datetime] = None


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
                "dvd": "2020-10-20 00:00:00",
                "website": "https://www.google.com",
                "production": "20th Century Fox",
                "lastupdated": "2020-10-20 00:00:00"
            }
        }

class TomatoesUpdate(BaseModel):
    viewer : Optional[Review]
    fresh : Optional[int]
    critic : Optional[Review]
    rotten : Optional[int]
    dvd : Optional[datetime]
    website : Optional[str]
    production : Optional[str]
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
                "dvd": "2020-10-20 00:00:00",
                "website": "https://www.google.com",
                "production": "20th Century Fox",
                "lastupdated": "2020-10-20 00:00:00"
            }
        }

