from typing import List

from fastapi import APIRouter, Request

from models.Movies import Movie, MovieUpdate

router = APIRouter()


@router.get("/", response_description="List all movies", response_model=List[Movie])
def list_movies(request: Request):
    movies = list(request.app.database["movies"].find(limit=150))
    return movies


@router.get("/movie", response_description="Get a specific movie by title or actor", response_model=Movie)
def get_movie(request: Request, title: str = None, actor: str = None):
    query = {}
    if title:
        query["title"] = title
    elif actor:
        query["cast"] = {"$in": [actor]}

    movie = request.app.database["movies"].find_one(query)

    return movie


@router.put("/movie/{title}", response_description="Update a movie")
def update_movie(request: Request, title: str, movie_update: MovieUpdate):
    update_data = {k: v for k, v in movie_update.dict().items() if v is not None}
    result = request.app.database["movies"].update_one({"title": title}, {"$set": update_data})

    return {"message": "Movie updated successfully"}


@router.get("/common-movies", response_description="Number of movies common in MongoDB and Neo4j")
def common_movies(request: Request):
    # Get all movie titles from MongoDB
    mongo_movies = set(movie["title"] for movie in request.app.database["movies"].find({}, {"title": 1}))

    # Get all movie titles from Neo4j
    neo4j_query = "MATCH (m:Movie) RETURN m.title AS title"
    with request.app.neo4j_driver.session() as session:
        neo4j_movies = set(record["title"] for record in session.run(neo4j_query))

    # Find common movies
    common_count = len(mongo_movies.intersection(neo4j_movies))

    return {"common_movie_count": common_count}


@router.get("/movie-ratings/{title}", response_description="List users who rated a movie")
def list_users_who_rated_movie(request: Request, title: str):
    neo4j_query = """
        MATCH (u:User)-[:RATED]->(m:Movie {title: $title})
        RETURN u.name AS username
    """
    with request.app.neo4j_driver.session() as session:
        users = [record["username"] for record in session.run(neo4j_query, title=title)]

    return {"users": users}


@router.get("/user-ratings/{username}", response_description="Get user's rating info")
def get_user_ratings(request: Request, username: str):
    neo4j_query = """
        MATCH (u:User {name: $username})-[:RATED]->(m:Movie)
        RETURN m.title AS movie_title
    """
    with request.app.neo4j_driver.session() as session:
        movies = [record["movie_title"] for record in session.run(neo4j_query, username=username)]

    return {"username": username, "rated_movies_count": len(movies), "rated_movies": movies}
