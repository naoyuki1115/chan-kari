from typing import Union

from model import Base
from model.timestamp import Timestamp
from sqlalchemy import Column, Date, ForeignKey, Index, Integer
from sqlalchemy.orm import relationship


class Rental(Base, Timestamp):
    __tablename__ = "rentals"
    id: Union[int, Column] = Column(Integer, primary_key=True, autoincrement=True)
    user_id: Union[int, Column] = Column(
        Integer,
        ForeignKey("users.id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False,
    )
    item_id: Union[int, Column] = Column(
        Integer,
        ForeignKey("items.id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False,
    )
    rented_at: Union[Date, Column] = Column(Date, nullable=False)
    return_plan_date: Union[Date, Column] = Column(Date, nullable=False)
    returned_at: Union[Date, Column] = Column(Date, nullable=True)

    users = relationship("User", back_populates="rentals")
    items = relationship("Item", back_populates="rentals")

    __table_args__ = (
        Index(
            "uix_rental_when_returned_at_is_null",
            "item_id",
            unique=True,
            postgresql_where=returned_at.is_(None),  # type:ignore
        ),
    )
