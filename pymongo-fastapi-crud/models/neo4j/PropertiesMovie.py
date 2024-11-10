from pydantic import BaseModel, Field


class PropertiesMovie(BaseModel):
    tagline: str = Field(...)
    title: str = Field(...)
    released: str = Field(...)

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "tagline": "Welcome to the Real World",
                "title": "The Matrix",
                "released": "1999"
            }
        }
