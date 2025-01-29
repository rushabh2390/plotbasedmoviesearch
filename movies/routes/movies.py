from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_, func, select
from typing import List, Optional
from movies.models import movies as movie_model
from movies.schemas import movies as movie_schemas
from config.config import settings
from database.database import engine, get_db
import numpy as np
import requests
import time

# Load the .env file
hf_token = settings.HF_TOKEN
embedding_url = settings.EMBEDDING_URL
router = APIRouter(
    prefix="/movies"
)


def generate_embedding(text: str) -> list[float]:
    time.sleep(10)
    response = requests.post(embedding_url, headers={
                             "Authorization": f"Bearer {hf_token}"}, json={"inputs": text}, timeout=30)
    if response.status_code != 200:
        raise ValueError(
            f"Response failed with status code {response.status_code}:{response.text} {hf_token}")
    return response.json()


@router.post("/recommendation", response_model=list[movie_schemas.Movie])
def read_user(search: movie_schemas.Search, db: Session = Depends(get_db)):
    embedding_search = np.array(generate_embedding(search.plot_search))
    db_movies = db.scalars(select(movie_model.Movie).order_by(
        movie_model.Movie.plot_embedding_hf.l2_distance(embedding_search)).limit(5)).all()

    if not db_movies:
        raise HTTPException(
            status_code=404, detail="No movie found near to plot search")
    return db_movies