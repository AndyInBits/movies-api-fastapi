from schemas.movie import Movie
from models.movies import Movie as MovieModel


class MovieService:
    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self) -> list[Movie]:
        result = self.db.query(MovieModel).all()
        return result
    
    def get_movie(self, id) -> list[Movie]:
        result = self.db.query(MovieModel).filter(MovieModel.id == id).all()
        return result
    
    def get_movie_by_category(self, category) -> list[Movie]:
        result = self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return result
    
    def create_movie(self, movie: Movie) -> None:
        new_movie = MovieModel(**movie.model_dump())
        self.db.add(new_movie)
        self.db.commit()
        return
    
    def update_movie(self, movie_param: Movie, id: int) -> None:
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        movie.title = movie_param.title
        movie.overview = movie_param.overview
        movie.category = movie_param.category
        movie.year = movie_param.year
        movie.rating = movie_param.rating
        self.db.commit()
        return

    def delete_movie(self, id : int):
        self.db.query(MovieModel).filter(MovieModel.id == id).delete()
        self.db.commit()
        return
