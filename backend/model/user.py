from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from model import Base
from model.timestamp import Timestamp


class UserDTO(Base, Timestamp):
    __tablename__ = "users"
    id: int = Column(Integer, primary_key=True, autoincrement=True)  # type: ignore
    name: str = Column(String, nullable=False)  # type: ignore
    email: str = Column(String, nullable=False, unique=True)  # type: ignore
    image_url: str = Column(String, nullable=True)  # type: ignore

    items = relationship("ItemDTO", back_populates="owner")
    rentals = relationship("RentalDTO", back_populates="user")
