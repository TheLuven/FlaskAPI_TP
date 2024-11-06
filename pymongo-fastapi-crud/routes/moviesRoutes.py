from typing import List

from fastapi import APIRouter, Request

from models.Movies import Movie

router = APIRouter()


@router.get("/", response_description="List all movies", response_model=List[Movie])
def list_movies(request: Request):
    movies = list(request.app.database["movies"].find(limit=100))
    return movies
