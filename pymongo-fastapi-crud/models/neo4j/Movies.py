from pydantic import BaseModel, Field

from models.neo4j.PropertiesMovie import PropertiesMovie


class Movie(BaseModel):
    identity: int = Field(...)
    labels: list[str] = Field(...)
    properties: PropertiesMovie = Field(...)
    elementId: str = Field(...)

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "identity": 0,
                "labels": ["Movie"],
                "properties": {
                    "tagline": "Welcome to the Real World",
                    "title": "The Matrix",
                    "released": "1999"
                },
                "elementId": "0"
            }
        }