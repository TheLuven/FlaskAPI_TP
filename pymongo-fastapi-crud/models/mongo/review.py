from typing import Optional

from pydantic import BaseModel, Field


class Review(BaseModel):
    rating: float = Field(...)
    numReviews: int = Field(...)
    meter: Optional[int] = None

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "rating": 4.5,
                "numReviews": 100,
                "meter": 80
            }
        }

class ReviewUpdate(BaseModel):
    rating : Optional[float]
    numReviews : Optional[int]
    meter : Optional[int]

    class Config:
        json_schema_extra = {
            "example": {
                "rating": 4.5,
                "numReviews": 100,
                "meter": 80
            }
        }

