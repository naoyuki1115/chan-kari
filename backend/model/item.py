from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from model import Base
from model.timestamp import Timestamp


class Item(Base, Timestamp):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    owner_id = Column(
        Integer,
        ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )
    user = relationship("User", back_populates="items")
    available = Column(Boolean, nullable=False)
    image_url = Column(String, nullable=True)
    description = Column(String, nullable=True)
    author = Column(String, nullable=True)

    rental = relationship("Rental", back_populates="items")
