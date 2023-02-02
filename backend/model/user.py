from model import Base
from model.timestamp import Timestamp
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(Base, Timestamp):
    __tablename__ = "users"
    id: int = Column(Integer, primary_key=True, autoincrement=True)  # type:ignore
    name: str = Column(String, nullable=False)  # type:ignore
    email: str = Column(String, nullable=False, unique=True)  # type:ignore
    image_url: str = Column(String, nullable=True)  # type:ignore

    items = relationship("Item", back_populates="users")
    rentals = relationship("Rental", back_populates="users")

    id: int
