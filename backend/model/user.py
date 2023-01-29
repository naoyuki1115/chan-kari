from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from model import Base
from model.timestamp import Timestamp


class User(Base, Timestamp):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    image_url = Column(String, nullable=True)

    item = relationship("Item", back_populates="users")
    rental = relationship("Rental", back_populates="users")
