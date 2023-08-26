from pydantic import BaseModel, PrivateAttr


class Movie(BaseModel):
    _id: int = PrivateAttr()
    title: str
    overview: str
    year: int
    rating: float
    category: str