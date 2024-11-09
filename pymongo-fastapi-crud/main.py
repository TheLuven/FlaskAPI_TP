from fastapi import FastAPI
from dotenv import dotenv_values

from pymongo import MongoClient
from pymongo.server_api import ServerApi

from neo4j import GraphDatabase

from routes.booksRoutes import router as book_router
from routes.artistsRoutes import router as artist_router
from routes.moviesRoutes import router as movie_router

config = dotenv_values(".env")

app = FastAPI()



@app.on_event("startup")
def startup_db_client():
    print("Connecting to MongoDB...")
    app.mongodb_client = MongoClient(
        config["ATLAS_URI"],
        server_api=ServerApi('1')
    )
    try:
        app.mongodb_client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        app.database = app.mongodb_client[config["DB_NAME"]]
        print("Connected to the database")
    except Exception as e:
        print("Exception", e)
        print("Couldn't connect to MongoDB")

    try:
        print("Connecting to neo4j...")
        app.neo4j_client = GraphDatabase.driver(config["NEO4J_URI"], auth=(config["NEO4J_USER"], config["NEO4J_PASSWORD"]))
        app.neo4j_client.verify_connectivity()
        print("Connection established.")
        app.neo4j_session = app.neo4j_client.session(database="neo4j")
        print("Connected to neo4j")
    except Exception as e:
        print("Exception", e)
        print("Couldn't connect to neo4j")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
    print("Connection to MongoDB closed")
    app.neo4j_session.close()
    app.neo4j_client.close()
    print("Connection to Neo4j closed")



app.include_router(movie_router, tags=["movies"], prefix="/movies")
app.include_router(book_router, tags=["books"], prefix="/books")
app.include_router(artist_router, tags=["artists"], prefix="/artists")
