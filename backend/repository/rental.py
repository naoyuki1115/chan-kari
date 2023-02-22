import abc
from typing import Optional

import model
from schema import PaginationQuery


class RentalStoreInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def list_valid(self) -> list[model.Rental]:
        raise NotImplementedError()

    @abc.abstractmethod
    def list_by_user_id(
        self,
        user_id: int,
        closed: bool,
        pagination: PaginationQuery,
    ) -> list[model.Rental]:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(self) -> list[model.Rental]:
        raise NotImplementedError()

    @abc.abstractmethod
    def detail(self, id: int) -> Optional[model.Rental]:
        raise NotImplementedError()

    @abc.abstractmethod
    def create(self, rental: model.Rental) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, rental: model.Rental) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self) -> None:
        raise NotImplementedError()
