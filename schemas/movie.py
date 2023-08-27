from typing import Optional
from pydantic import BaseModel, Field


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(max_length=50)
    overview: str = Field(default="Description movie", min_length=10, max_length=255)
    year: int = Field(default=2022, le=2023, ge=1950)
    rating: float = Field(default=0.0, le=10.0, ge=0.0)
    category: str = Field(min_length=5, max_length=15)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Thor: Ragnarok",
                "overview": "Thor se encuentra atrapado en un planeta distante y debe luchar en una arena mortal.",
                "year": 2017,
                "rating": 7.9,
                "category": "Acción",
            }
        }
