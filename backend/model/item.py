from typing import Union

from model import Base
from model.timestamp import Timestamp
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Item(Base, Timestamp):
    __tablename__ = "items"
    id: Union[int, Column] = Column(Integer, primary_key=True, autoincrement=True)
    name: Union[str, Column] = Column(String, nullable=False)
    owner_id: Union[int, Column] = Column(
        Integer,
        ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )
    available: Union[bool, Column] = Column(Boolean, nullable=False)
    image_url: Union[str, Column] = Column(String, nullable=True)
    description: Union[str, Column] = Column(String, nullable=True)
    author: Union[str, Column] = Column(String, nullable=True)

    users = relationship("User", back_populates="items")
    rentals = relationship("Rental", back_populates="items")
