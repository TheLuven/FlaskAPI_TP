from typing import Optional

from pydantic import BaseModel, Field


class Award(BaseModel):
    wins : int = Field(...)
    nominations : int = Field(...)
    text : str = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "wins": 10,
                "nominations": 20,
                "text": "10 wins & 20 nominations."
            }
        }

class AwardUpdate(BaseModel):
    wins : Optional[int]
    nominations : Optional[int]
    text : Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "wins": 10,
                "nominations": 20,
                "text": "10 wins & 20 nominations."
            }
        }
