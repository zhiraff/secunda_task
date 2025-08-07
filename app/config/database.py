from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from .settings import settings

engine = create_engine(
    settings.POSTGRES_CONNECTION_STRING,
    # connect_args={"check_same_thread": False},
)

async_engine = create_async_engine(
    settings.POSTGRES_CONNECTION_STRING_ASYNC,
    # connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

SessionLocal_async = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=async_engine,
)

Base = declarative_base()


def get_db():
    """
    Create a database session.

    Yields:
        Session: The database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_db_async():
    """
    Create a database session.

    Yields:
        Session: The database session.
    """
    db = SessionLocal_async()
    try:
        yield db
    finally:
        db.close()
