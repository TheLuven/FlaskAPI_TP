from typing import List, Optional

from pydantic import BaseModel, Field

from models.neo4j.Properties import Properties


class User(BaseModel):
    identity: Optional[int] = None
    labels: List[str] = Field(...)
    properties: Properties = Field(...)
    elementId: str = Field(...)

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "identity": 0,
                "labels": ["User"],
                "properties": {
                    "born": "1985",
                    "name": "Keanu Reeves"
                },
                "elementId": "0"
            }
        }
