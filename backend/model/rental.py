from model import Base
from model.timestamp import Timestamp
from sqlalchemy import Column, Date, ForeignKey, Index, Integer
from sqlalchemy.orm import relationship


class Rental(Base, Timestamp):
    __tablename__ = "rentals"
    id: int = Column(Integer, primary_key=True, autoincrement=True)  # type:ignore
    user_id: int = Column(
        Integer,
        ForeignKey("users.id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False,
    )  # type:ignore
    item_id: int = Column(
        Integer,
        ForeignKey("items.id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False,
    )  # type:ignore
    rented_at: Date = Column(Date, nullable=False)  # type:ignore
    return_plan_date: Date = Column(Date, nullable=False)  # type:ignore
    returned_at: Date = Column(Date, nullable=True)  # type:ignore

    users = relationship("User", back_populates="rentals")
    items = relationship("Item", back_populates="rentals")

    __table_args__ = (
        Index(
            "uix_rental_when_returned_at_is_null",
            "user_id",
            "item_id",
            "rented_at",
            unique=True,
            postgresql_where=returned_at.is_(None),  # type:ignore
        ),
    )
