from utils import movies
from typing import Optional
from pydantic import BaseModel, PrivateAttr, Field


class Movie(BaseModel):
    id: Optional[int]
    title: str = Field(max_length=15)
    overview: str = Field(default="Description movie", min_length=10, max_length=50)
    year: int = Field(default=2022, le=2023, ge=1950)
    rating: float = Field(default=0.0, le=5.0, ge=0.0)
    category: str = Field(min_length=5, max_length=15)

    class Config:
        json_schema_extra = {
            "example": {
                "id": len(movies)+1,
                "title": "My movie",
                "overview": "Description movie",
                "year": 2022,
                "rating": 4.5,
                "category": "Action",
            }
        }
