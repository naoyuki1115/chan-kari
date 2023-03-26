import abc
from typing import Optional

from domain import Rental
from schema import PaginationQuery


class RentalStoreInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def list_valid(self) -> list[Rental]:
        raise NotImplementedError()

    @abc.abstractmethod
    def list_by_user_id(
        self,
        user_id: int,
        closed: bool,
        pagination: PaginationQuery,
    ) -> list[Rental]:
        raise NotImplementedError()

    @abc.abstractmethod
    def detail(self, id: int) -> Optional[Rental]:
        raise NotImplementedError()

    @abc.abstractmethod
    def create(self, rental: Rental) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, rental: Rental) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self) -> None:
        raise NotImplementedError()
