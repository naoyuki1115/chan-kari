from sqlalchemy import Column, Date, ForeignKey, Index, Integer
from sqlalchemy.orm import relationship

from model import Base
from model.timestamp import Timestamp


class Rental(Base, Timestamp):
    __tablename__ = "rentals"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(
        Integer,
        ForeignKey("users.id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False,
    )
    user = relationship("User", back_populates="rentals")
    item_id = Column(
        Integer,
        ForeignKey("items.id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False,
    )
    item = relationship("Item", back_populates="rentals")
    rented_at = Column(Date, nullable=False)
    return_plan_date = Column(Date, nullable=False)
    returned_at = Column(Date, nullable=True)

    __table_args__ = (
        Index(
            "uix_rental_when_returned_at_is_null",
            "user_id",
            "item_id",
            "rented_at",
            unique=True,
            postgresql_where=returned_at.is_(None),
        ),
    )
