import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

db_url = "postgresql://%s:%s@%s:%s/%s?charset=utf8" % (
    os.environ.get("POSTGRES_USER"),
    os.environ.get("POSTGRES_PASSWORD"),
    os.environ.get("POSTGRES_HOST"),
    os.environ.get("POSTGRES_PORT"),
    os.environ.get("POSTGRES_DB"),
)

engine = create_engine(db_url, echo=True)

Base = declarative_base()
