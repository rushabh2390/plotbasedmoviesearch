from pydantic import BaseModel, ValidationError, field_validator, Json, Field
from pgvector.sqlalchemy import Vector
from typing import Optional
from datetime import datetime
from passlib.context import CryptContext
from typing import List

class Movie(BaseModel):
    id: Optional[int] = None
    oid: Optional[str] = None
    plot: Optional[str] = None
    runtime: Optional[int] = None
    genres: Optional[list] = None
    casting: Optional[list] = None
    num_mflix_comments: Optional[int] = None
    title: Optional[str] = None
    fullplot: Optional[str] = None
    countries: Optional[list] = None
    released: Optional[datetime] = None
    directors: Optional[list] = None
    rated: Optional[str] = None
    awards: Optional[dict] = None
    lastupdated: Optional[datetime] = None
    year: Optional[int] = None
    imdb: Optional[dict] = None
    type: Optional[str] = None
    tomatoes: Optional[dict] = None
    writers: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    fullname: Optional[str] = None
    email: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    is_super_user: Optional[bool] = False
    is_staff_user: Optional[bool] = False

    class Config:
        from_attributes = True

class Search(BaseModel):
    plot_search: Optional[str] = None

class MovieList(BaseModel):
    movies: List[Movie]