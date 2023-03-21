from typing import Optional

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from domain import Item, ItemStatus
from model import Base
from model.timestamp import Timestamp


class ItemDTO(Base, Timestamp):
    __tablename__ = "items"
    id: int = Column(Integer, primary_key=True, autoincrement=True)  # type: ignore
    name: str = Column(String, nullable=False)  # type: ignore
    owner_id: int = Column(  # type: ignore
        Integer,
        ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )
    available: bool = Column(Boolean, nullable=False)  # type: ignore
    image_url: Optional[str] = Column(String, nullable=True)  # type: ignore
    description: Optional[str] = Column(String, nullable=True)  # type: ignore
    author: Optional[str] = Column(String, nullable=True)  # type: ignore

    users = relationship("UserDTO", back_populates="items")
    rentals = relationship("RentalDTO", back_populates="items")

    @classmethod
    def from_domain_model(cls, item: Item):
        if item.get_status() == ItemStatus.private:
            available = False
        else:
            available = True
        return cls(
            id=item.get_id(),
            name=item.get_name(),
            owner_id=item.get_owner_id(),
            available=available,
            imageUrl=item.get_image_url(),
            description=item.get_description(),
            author=item.get_author(),
        )

    def to_domain_model(self) -> Item:
        item = Item(
            name=self.name,
            owner_id=self.owner_id,
            image_url=self.image_url,
            description=self.description,
            author=self.author,
        )
        item.set_id(self.id)
        self.__judge_status(item)
        return item

    def __judge_status(self, item: Item):
        if self.available is False:
            item.set_private_status()
        elif len(list(filter(lambda r: r.returned_date is None, self.rentals))) > 0:
            item.set_rented_status()
        else:
            item.set_public_status()
