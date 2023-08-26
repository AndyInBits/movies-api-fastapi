from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import JSONResponse, HTMLResponse
from models import Movie
from utils import movies

app = FastAPI()

app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"


@app.get("/", tags=['Home'])
def hello_world():
    return HTMLResponse(content="<h1>FastAPI</h1><p>Esta es mi primera aplicacion con FastAPI</p>", status_code=200)

@app.get("/movies", tags=['Movies'], response_model=list)
def get_movies() -> list:
    return JSONResponse(content=movies, status_code=200)

@app.get("/movies/{id}", tags=['Movies'], response_model=Movie)
def get_movie(id: int = Path(..., gt=1, le=2000)) -> Movie:
    movie = list(filter(lambda x: x['_id'] == id,movies))
    return JSONResponse(content=movie, status_code=200) if len(movie) > 0 else JSONResponse(content={}, status_code=404) 

@app.get("/movies/", tags=['Movies'], response_model=Movie)
def get_movie_by_category(category_name: str = Query(..., min_length=5, max_length=15)) -> Movie:
    movie = list(filter(lambda x: x['category'] == category_name,movies))
    return JSONResponse(content=movie, status_code=200) if len(movie) > 0 else JSONResponse(content={}, status_code=404) 

@app.post("/movies", tags=['Movies'], response_model = list[Movie])
def create_movie(movie: Movie = Body(...)) -> list[Movie]:
    new_movie = {
        "id": len(movies)+1,
        "title": movie.title,
        "overview": movie.overview,
        "year": movie.year,
        "rating": movie.rating,
        "category": movie.category
    }
    movies.append(new_movie)
    return JSONResponse(content=movies, status_code=200)

@app.put("/movies/{id}", tags=['Movies'], response_model = list[Movie])
def update_movie(id: int, movie_param: Movie = Body(...)) -> list[Movie]:
    movie = list(filter(lambda x: x['id'] == id,movies))
    movie[0] = movie_param
    return JSONResponse(content=movies, status_code=200)

@app.delete("/movies/{id}", tags=['Movies'], response_model = dict)
def delete_movie(id: int) -> dict:
    movie = list(filter(lambda x: x['id'] == id,movies))
    movies.remove(movie[0])
    return JSONResponse(content={}, status_code=202)
