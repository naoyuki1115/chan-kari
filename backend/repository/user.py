import abc
from typing import Optional

from domain import User


class UserStoreInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def detailByUid(self, uid: str) -> Optional[User]:
        raise NotImplementedError()

    @abc.abstractmethod
    def create(self, user: User) -> None:
        raise NotImplementedError()
