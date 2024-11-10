from typing import List

from fastapi import APIRouter, Request

from models.neo4j.Users import User

router = APIRouter()

def serialize_node(node):
    return {
        "identity": node.element_id.split(":")[-1],
        "labels": list(node.labels),
        "properties": dict(node),
        "elementId": node.element_id
    }

@router.get("/rated/{movie_title}", response_description="Get users who rated a movie", response_model=List[User])
def get_users_rated_movie(movie_title: str, request: Request):
    users = list(request.app.neo4j_session.run("MATCH (p:Person)-[:REVIEWED]->(m:Movie {title: $movie_title}) RETURN p", movie_title=movie_title))
    serialized_users = [serialize_node(record["p"]) for record in users]
    return serialized_users

@router.get("/rated_by/{username}", response_description="Get users with the number of movies rated and a list of these movies", response_model=dict)
def get_user_rated_movies(username: str, request: Request):
    user = request.app.neo4j_session.run("MATCH (p:Person {name: $username}) RETURN p", username=username).single()
    movies = list(request.app.neo4j_session.run("MATCH (p:Person {name: $username})-[:REVIEWED]->(m:Movie) RETURN m", username=username))

    serialized_user = serialize_node(user["p"]) if user else None
    serialized_movies = [serialize_node(record["m"]) for record in movies]

    return {
        "user": serialized_user,
        "mumber_of_movies_rated": len(serialized_movies),
        "movies": serialized_movies
    }
