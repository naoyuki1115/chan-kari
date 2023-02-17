import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

db_url = "postgres://%s:%s@%s:%s/%s" % (
    os.environ.get("POSTGRES_USER"),
    os.environ.get("POSTGRES_PASSWORD"),
    os.environ.get("POSTGRES_HOST"),
    os.environ.get("POSTGRES_PORT"),
    os.environ.get("POSTGRES_DB"),
)

engine = create_engine(db_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def create_table():
    Base.metadata.create_all(engine)


def drop_table():
    Base.metadata.drop_all(engine)


def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
