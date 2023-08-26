from typing import Optional
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from models import Movie
from utils import movies

app = FastAPI()

app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"


@app.get("/", tags=['Home'])
def hello_world():
    return HTMLResponse(content="<h1>FastAPI</h1><p>Esta es mi primera aplicacion con FastAPI</p>", status_code=200)

@app.get("/movies", tags=['Movies'])
def get_movies():
    return movies


@app.get("/movies/{id}", tags=['Movies'])
def get_movie(id: int):
    movie = list(filter(lambda x: x['_id'] == id,movies))
    return movie[0] if len(movie) > 0 else "No hay nada que ver"

@app.get("/movies/", tags=['Movies'])
def get_movie_by_category(category_name: str, year: Optional[int]= None):
    movie = list(filter(lambda x: x['category'] == category_name,movies))
    return movie[0] if len(movie) > 0 else "No hay nada que ver"

@app.post("/movies", tags=['Movies'])
def create_movie(movie: Movie = Body(...)):
    movies.append(movie)
    return movie

@app.put("/movies/{id}", tags=['Movies'])
def update_movie(id: int, movie_param: Movie = Body(...)):
    movie = list(filter(lambda x: x['_id'] == id,movies))
    movie[0] = movie_param
    return movie[0] if len(movie) > 0 else "No hay nada que ver"

@app.delete("/movies/{id}", tags=['Movies'])
def delete_movie(id: int):
    movie = list(filter(lambda x: x['_id'] == id,movies))
    movies.remove(movie[0])
    return movies if len(movies) > 0 else "No hay nada que ver"
