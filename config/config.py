import logging
import os
from dotenv import load_dotenv
load_dotenv()


class Settings:
    DB_NAME = os.getenv("DATABASE_NAME", "inventory_db")
    DB_USER = os.getenv("DATABASE_USER", "postgres")
    DB_PASSWORD = os.getenv("DATABASE_PASSWORD", "postgres")
    DB_HOST = os.getenv("DATABASE_HOST", "localhost")
    DB_PORT = os.getenv("DATABASE_PORT", "5432")
    DATABASE_URL = os.getenv("DATABASE_URL", "5432")
    HF_TOKEN = os.getenv("HF_TOKEN", None)
    EMBEDDING_URL = os.getenv(
        "EMBEDDING_URL", "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2")


settings = Settings()
