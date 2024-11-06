import uuid
from typing import Optional, List

from pydantic import BaseModel, Field

from models.Award import Award
from models.imdb import Imdb
from models.tomatoes import Tomatoes


class Movie(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    plot: str = Field(...)
    genres: [str] = Field(...)
    runtime: int = Field(...)
    title: str = Field(...)
    fullplot: str = Field(...)
    languages: [str] = Field(...)
    released: str = Field(...)
    directors: [str] = Field(...)
    rated = str = Field(...)
    awards: Award = Field(...)
    lastupdated: str = Field(...)
    year: int = Field(...)
    imdb: Imdb = Field(...)
    countries: [str] = Field(...)
    type: str = Field(...)
    tomatoes: Tomatoes = Field(...)
    num_mflix_comments: int = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "plot": "In a galaxy far far away",
                "genres": ["Sci-Fi", "Action"],
                "runtime": 120,
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

class MovieUpdate(BaseModel):
    plot : Optional[str]
    genres : Optional[List[str]]
    runtime : Optional[int]
    title : Optional[str]
    fullplot : Optional[str]
    languages : Optional[List[str]]
    released : Optional[str]
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