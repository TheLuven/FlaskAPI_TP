from typing import Optional

from pydantic import BaseModel, Field


class Properties(BaseModel):
    born: Optional[str] = None
    name : str = Field(...)

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "born": "1985",
                "name": "Keanu Reeves"
            }
        }