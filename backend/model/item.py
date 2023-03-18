import domain_model
from model import Base, Rental, User
from model.timestamp import Timestamp
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.domain_model.item import ItemStatus


class Item(Base, Timestamp):
    __tablename__ = "items"
    id: int = Column(Integer, primary_key=True, autoincrement=True)  # type: ignore
    name: str = Column(String, nullable=False)  # type: ignore
    owner_id: int = Column(  # type: ignore
        Integer,
        ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )
    available: bool = Column(Boolean, nullable=False)  # type: ignore
    image_url: str = Column(String, nullable=True)  # type: ignore
    description: str = Column(String, nullable=True)  # type: ignore
    author: str = Column(String, nullable=True)  # type: ignore

    user: User = relationship("User", back_populates="items")
    rentals: list[Rental] = relationship("Rental", back_populates="item")

    users = relationship("User", back_populates="items")
    rentals = relationship("Rental", back_populates="items")
