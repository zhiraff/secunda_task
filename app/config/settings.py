import os
from typing import Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """
    Application settings.
    """
    # FastAPI
    # Debug should be set to False on production
    DEBUG: Optional[bool] = os.getenv("DEBUG", True)
    # Title is the name of application
    TITLE: Optional[str] = os.getenv("TITLE", 'Тестовое задание для Secunda')
    # Origins
    ORIGINS: Optional[str] = os.getenv("ORIGINS", '*')
    # PostgreSQL connection string
    POSTGRESS_USER: Optional[str] = os.getenv("POSTGRES_USER", "secunda")
    POSTGRESS_PASSWORD: Optional[str] = os.getenv("POSTGRES_PASSWORD", "secunda")
    POSTGRES_PORT: Optional[str] = os.getenv("POSTGRES_PORT", "5432")
    POSTGRES_DB: Optional[str] = os.getenv("POSTGRES_DB", "secunda")
    POSTGRES_HOST: Optional[str] = os.getenv("POSTGRES_HOST", "192.168.0.102")
    POSTGRES_CONNECTION_STRING: str = f"postgresql+psycopg2://{POSTGRESS_USER}:{POSTGRESS_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    POSTGRES_CONNECTION_STRING_ASYNC: str = f"postgresql+asyncpg://{POSTGRESS_USER}:{POSTGRESS_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    SITE_DOMAIN: str = os.getenv("SITE_DOMAIN", "http://localhost:5000")
    SITE_PREFIX: str = os.getenv("SITE_PREFIX", "")
    API_KEY: str = os.getenv("API_KEY", "qwerty123")


settings = Settings()
