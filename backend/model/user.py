from typing import Union

from model import Base
from model.timestamp import Timestamp
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(Base, Timestamp):
    __tablename__ = "users"
    id: Union[int, Column] = Column(Integer, primary_key=True, autoincrement=True)
    name: Union[str, Column] = Column(String, nullable=False)
    email: Union[str, Column] = Column(String, nullable=False, unique=True)
    image_url: Union[str, Column] = Column(String, nullable=True)

    items = relationship("Item", back_populates="users")
    rentals = relationship("Rental", back_populates="users")
