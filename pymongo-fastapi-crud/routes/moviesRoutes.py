from typing import List

from fastapi import APIRouter, Request, HTTPException

from models.Movies import Movie, MovieUpdate

router = APIRouter()


@router.get("/", response_description="List all movies", response_model=List[Movie])
def list_movies(request: Request):
    movies = list(request.app.database["movies"].find(limit=150))
    return movies

@router.get("/{title0rActor}", response_description="Get a specific movie by title or actor", response_model=List[Movie])
def get_movie(request: Request, title0rActor: str):
    query = {}
    if title0rActor:
        query["$or"] = [{"title": {"$regex": title0rActor, "$options": "i"}}, {"cast": {"$regex": title0rActor, "$options": "i"}}]

    movie = list(request.app.database["movies"].find(query))

    return movie

@router.put("/{title}", response_description="Update a movie", response_model=Movie)
def update_movie(title: str, request: Request, movie: MovieUpdate):
    movie_find = request.app.database["movies"].find_one({"title": title})
    print(movie.dict(exclude_unset=True))
    if movie_find:
        update_result = request.app.database["movies"].update_one(
            {"title": title}, {"$set": movie.dict(exclude_unset=True)}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=404, detail=f"Movie with title {title} not update")

        updated_movie = request.app.database["movies"].find_one({"title": title})
        return updated_movie
    else:
        raise HTTPException(status_code=404, detail=f"Movie with title {title} not found")
