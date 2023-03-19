from datetime import date
from typing import Optional

import domain_model
from model import Base, Item, User
from model.timestamp import Timestamp
from sqlalchemy import Column, Date, ForeignKey, Index, Integer
from sqlalchemy.orm import relationship


class Rental(Base, Timestamp):
    __tablename__ = "rentals"
    id: int = Column(Integer, primary_key=True, autoincrement=True)  # type: ignore
    user_id: int = Column(  # type: ignore
        Integer,
        ForeignKey("users.id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False,
    )
    item_id: int = Column(  # type: ignore
        Integer,
        ForeignKey("items.id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False,
    )
    rented_date: date = Column(Date, nullable=False)  # type: ignore
    return_plan_date: date = Column(Date, nullable=False)  # type: ignore
    returned_date: Optional[date] = Column(Date, nullable=True)  # type: ignore

    user: User = relationship("User", back_populates="rentals")
    item: Item = relationship("Item", back_populates="rentals")

    __table_args__ = (
        Index(
            "uix_rental_when_returned_date_is_null",
            "item_id",
            unique=True,
            postgresql_where=returned_date.is_(None),  # type:ignore
        ),
    )

    @classmethod
    def from_domain_model(cls, rental: domain_model.Rental):
        return cls(
            id=rental.get_id(),
            user_id=rental.get_user_id(),
            item_id=rental.get_item().get_id(),
            rented_date=rental.get_rented_date(),
            return_plan_date=rental.get_return_plan_date(),
            returned_date=rental.get_returned_date(),
        )
