import abc
from typing import Optional

import domain_model
from schema import PaginationQuery


class RentalStoreInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def list_valid(self) -> list[domain_model.Rental]:
        raise NotImplementedError()

    @abc.abstractmethod
    def list_by_user_id(
        self,
        user_id: int,
        closed: bool,
        pagination: PaginationQuery,
    ) -> list[domain_model.Rental]:
        raise NotImplementedError()

    @abc.abstractmethod
    def detail(self, id: int) -> Optional[domain_model.Rental]:
        raise NotImplementedError()

    @abc.abstractmethod
    def create(self, rental: domain_model.Rental) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, rental: domain_model.Rental) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self) -> None:
        raise NotImplementedError()
