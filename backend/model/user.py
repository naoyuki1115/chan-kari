from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from domain import User
from model import Base
from model.timestamp import Timestamp


class UserDTO(Base, Timestamp):
    __tablename__ = "users"
    id: int = Column(Integer, primary_key=True, autoincrement=True)  # type: ignore
    uid: str = Column(String, nullable=False, unique=True)  # type: ignore
    name: str = Column(String, nullable=False)  # type: ignore
    email: str = Column(String, nullable=False, unique=True)  # type: ignore
    image_url: str = Column(String, nullable=True)  # type: ignore

    items = relationship("ItemDTO", back_populates="owner")
    rentals = relationship("RentalDTO", back_populates="user")

    @classmethod
    def from_domain_model(cls, user: User):
        return cls(
            uid=user.get_uid(),
            name=user.get_name(),
            email=user.get_email(),
            image_url=user.get_image_url(),
        )

    def to_domain_model(self) -> User:
        user = User(
            uid=self.uid,
            name=self.name,
            email=self.email,
            image_url=self.image_url,
            id=self.id,
        )
        return user
