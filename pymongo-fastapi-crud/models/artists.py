import uuid
from typing import Optional, List
from pydantic import BaseModel, Field

class Artist(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    last_name: str = Field(...)
    first_name: str = Field(...)
    birth_date: Optional[str] = None
    hobbies: Optional[List[str]] = None

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "last_name": "Smith",
                "first_name": "John",
                "birth_date": "1970",
                "hobbies": ["painting", "reading"]
            }
        }

class ArtistUpdate(BaseModel):
    last_name: Optional[str]
    first_name: Optional[str]
    birth_date: Optional[str]
    hobbies: Optional[List[str]]

    class Config:
        json_schema_extra = {
            "example": {
                "last_name": "Smith",
                "first_name": "John",
                "birth_date": "1970",
                "hobbies": ["painting", "reading"]
            }
        }