from fastapi import APIRouter, Depends, Path, Query, Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from config.database import Session

from schemas.movie import Movie
from middlewares.jwt_bearer import JWTBearer
from models.movies import Movie as MovieModel
from services.movie import MovieService

movie_router = APIRouter()


@movie_router.get("/movies", tags=["Movies"], response_model=list[Movie])
def get_movies() -> list[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@movie_router.get("/movie/{id}", tags=["Movies"], response_model=Movie)
def get_movie(id: int = Path(..., gt=1, le=2000)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(content={"msg": "Not Found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@movie_router.get("/movies/", tags=["Movies"], response_model=Movie)
def get_movie_by_category(
    category_name: str = Query(..., min_length=5, max_length=15)
) -> Movie:
    db = Session()
    result = MovieService(db).get_movie_by_category(category_name)
    if not result:
        return JSONResponse(content={"msg": "Not Found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@movie_router.post(
    "/movies", tags=["Movies"], response_model=str, status_code=201
)
def create_movie(movie: Movie = Body(...)) -> str:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(content="Created Movie", status_code=201)


@movie_router.put("/movies/{id}", tags=["Movies"], response_model=Movie)
def update_movie(id: int, movie_param: Movie = Body(...)) -> Movie:
    db = Session()
    movie = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not movie:
        return JSONResponse(content={"msg": "Not Found"}, status_code=404)
    MovieService(db).update_movie(movie_param, id)
    return JSONResponse(content={"msg": "Movie Modific"}, status_code=200)


@movie_router.delete("/movies/{id}", tags=["Movies"], response_model=dict)
def delete_movie(id: int) -> dict:
    db = Session()
    movie = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not movie:
        return JSONResponse(content={"msg": "Not Found"}, status_code=404)
    MovieService(db).delete_movie(id)
    return JSONResponse(content={"msg": "Deleted"}, status_code=200)
