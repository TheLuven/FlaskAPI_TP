from fastapi import FastAPI
from dotenv import dotenv_values
from nltk.corpus import movie_reviews
from pymongo import MongoClient
from pymongo.server_api import ServerApi

from routes.booksRoutes import router as book_router
from routes.artistsRoutes import router as artist_router
from routes.moviesRoutes import router as movie_router

config = dotenv_values(".env")
app = FastAPI()


@app.on_event("startup")
def startup_db_client():
    print("Connecting to MongoDB...")
    app.mongodb_client = MongoClient(config["ATLAS_URI"], server_api=ServerApi('1'))
    try:
        app.mongodb_client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        app.database = app.mongodb_client[config["DB_NAME"]]
        print("Connected to the database")
    except Exception as e:
        print("Exception", e)
        print("Couldn't connect to MongoDB")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
    print("Connection to MongoDB closed")


app.include_router(movie_router, tags=["movies"], prefix="/movies")
app.include_router(book_router, tags=["books"], prefix="/books")
app.include_router(artist_router, tags=["artists"], prefix="/artists")
