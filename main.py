from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from config.database import Base, engine
from middlewares.error_handler import ErrorHandler
from routes.movie import movie_router
from routes.auth import auth_router
from routes.healcheck import healcheck_router

app = FastAPI()

app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(healcheck_router)
app.include_router(auth_router)
app.include_router(movie_router)


Base.metadata.create_all(bind=engine)


