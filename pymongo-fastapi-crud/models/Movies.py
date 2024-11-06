import uuid
from datetime import datetime
from typing import Optional, List

from bson import ObjectId
from pydantic import BaseModel, Field

from models.Award import Award
from models.imdb import Imdb
from models.tomatoes import Tomatoes


class Movie(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    plot: Optional[str] = None
    genres: List[str] = Field(...)
    runtime: int = Field(...)
    cast : Optional[List[str]] = None
    poster : Optional[str] = None
    title: str = Field(...)
    fullplot: Optional[str] = None
    languages: Optional[List[str]] = None
    released: Optional[datetime] = None
    directors: List[str] = Field(...)
    rated: Optional[str] = None
    awards: Award = Field(...)
    lastupdated: str = Field(...)
    year: int = Field(...)
    imdb: Imdb = Field(...)
    countries: List[str] = Field(...)
    type: str = Field(...)
    tomatoes: Optional[Tomatoes] = None
    num_mflix_comments: int = Field(...)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str,
            datetime: lambda v: v.isoformat(),
        }
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "plot": "In a galaxy far far away",
                "genres": ["Sci-Fi", "Action"],
                "runtime": 120,
                "cast" : ["Mark Hamil","Harison Ford"],
                "poster" :"http://...",
                "title": "Star Wars",
                "fullplot": "The Empire is building a Death Star",
                "languages": ["English"],
                "released": "1977-03-23T00:00:00.000+00:00",
                "directors": ["George Lucas"],
                "rated": "PG",
                "awards": {
                    "wins": 10,
                    "nominations": 20,
                    "text": "10 wins & 20 nominations."
                },
                "lastupdated": "2020-10-20 00:00:00",
                "year": 1977,
                "imdb": {
                    "rating": 8.7,
                    "votes": 120000,
                    "id": 123456
                },
                "countries": ["USA"],
                "type": "movie",
                "tomatoes": {
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
                },
                "num_mflix_comments": 100,
            }
        }

class MovieUpdate(BaseModel):
    plot : Optional[str]
    genres : Optional[List[str]]
    runtime : Optional[int]
    cast : Optional[List[str]]
    poster: Optional[str]
    title : Optional[str]
    fullplot : Optional[str]
    languages : Optional[List[str]]
    released : Optional[datetime]
    directors : Optional[List[str]]
    rated : Optional[str]
    awards : Optional[Award]
    lastupdated : Optional[str]
    year : Optional[int]
    imdb : Optional[Imdb]
    countries : Optional[List[str]]
    type : Optional[str]
    tomatoes : Optional[Tomatoes]
    num_mflix_comments : Optional[int]

    class Config:
        json_schema_extra = {
            "example": {
                "plot": "In a galaxy far far away",
                "genres": ["Sci-Fi", "Action"],
                "runtime": 120,
                "cast": ["Mark Hamil", "Harison Ford"],
                "poster": "http://...",
                "title": "Star Wars",
                "fullplot": "The Empire is building a Death Star",
                "languages": ["English"],
                "released": "1977",
                "directors": ["George Lucas"],
                "rated": "PG",
                "awards": {
                    "wins": 10,
                    "nominations": 20,
                    "text": "10 wins & 20 nominations."
                },
                "lastupdated": "2020-10-20 00:00:00",
                "year": 1977,
                "imdb": {
                    "rating": 8.7,
                    "votes": 120000,
                    "id": 123456
                },
                "countries": ["USA"],
                "type": "movie",
                "tomatoes": {
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
                },
                "num_mflix_comments": 100,
            }
        }