from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List, Optional

from models.artists import Artist, ArtistUpdate

router = APIRouter()

@router.post("/", response_description="Create a new artist", status_code=status.HTTP_201_CREATED, response_model=Artist)
def create_artist(request: Request, artist: Artist = Body(...)):
    artist = jsonable_encoder(artist)
    new_artist = request.app.database["artists"].insert_one(artist)
    created_artist = request.app.database["artists"].find_one(
        {"_id": new_artist.inserted_id}
    )

    return created_artist

@router.get("/", response_description="List all artists", response_model=List[Artist])
def list_artists(request: Request):
    artists = list(request.app.database["artists"].find(limit=100))
    return artists

@router.get("/{id}", response_description="Get a single artist by id", response_model=Artist)
def find_artist(id: str, request: Request):
    if (artist := request.app.database["artists"].find_one({"_id": id})) is not None:
        return artist
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist with ID {id} not found")


@router.get("/search", response_description="Search for an artist by name or id", response_model=List[Artist])
def search_artist(request: Request, name: Optional[str] = None, id: Optional[str] = None):
    query = {}
    if name:
        query["$or"] = [{"first_name": name}, {"last_name": name}]
    if id:
        query["_id"] = id
    artists = list(request.app.database["artists"].find(query))
    if not artists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No artists found with the given criteria")

    return artists


@router.put("/{id}", response_description="Update an artist", response_model=Artist)
def update_artist(id: str, request: Request, artist: ArtistUpdate = Body(...)):
    artist = {k: v for k, v in artist.dict().items() if v is not None}
    if len(artist) >= 1:
        update_result = request.app.database["artists"].update_one(
            {"_id": id}, {"$set": artist}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist with ID {id} not found")

    if (
        existing_artist := request.app.database["artists"].find_one({"_id": id})
    ) is not None:
        return existing_artist

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist with ID {id} not found")

@router.delete("/{id}", response_description="Delete an artist")
def delete_artist(id: str, request: Request, response: Response):
    delete_result = request.app.database["artists"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist with ID {id} not found")