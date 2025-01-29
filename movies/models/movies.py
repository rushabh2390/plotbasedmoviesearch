from sqlalchemy import Boolean, Column, DateTime, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import TypeDecorator
from pgvector.sqlalchemy import Vector
import numpy as np
import json

Base = declarative_base()

# class Vector(TypeDecorator):
#     impl = String

#     def process_bind_param(self, value, dialect):
#         if value is not None:
#             value = json.dumps(value.tolist())  # Convert numpy array to JSON string
#         return value

#     def process_result_value(self, value, dialect):
#         if value is not None:
#             value = np.array(json.loads(value))  # Convert JSON string back to numpy array
#         return value

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    oid = Column(String, nullable=True)
    plot = Column(String, nullable=True)
    runtime = Column(Integer, nullable=True)
    genres = Column(String, nullable=True)
    casting = Column(String, nullable=True)
    num_mflix_comments = Column(Integer, nullable=True)
    title = Column(String, nullable=True)
    fullplot = Column(String, nullable=True)
    countries = Column(String, nullable=True)
    released = Column(DateTime, nullable=True)
    directors = Column(String, nullable=True)
    rated = Column(String, nullable=True)
    awards = Column(JSON, nullable=True)
    lastupdated = Column(DateTime, nullable=True)
    year = Column(Integer, nullable=True)
    imdb = Column(JSON, nullable=True)
    type = Column(String, nullable=True)
    tomatoes = Column(JSON, nullable=True)
    plot_embedding_hf = Column(Vector, nullable=True)
    writers = Column(String, nullable=True)
