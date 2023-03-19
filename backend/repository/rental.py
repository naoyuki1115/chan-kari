import abc
from typing import Optional

import domain_model
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
    def list_by_user_id2(
        self,
        user_id: int,
        closed: bool,
        pagination: PaginationQuery,
    ) -> list[domain_model.Rental]:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(self) -> list[model.Rental]:
        raise NotImplementedError()

    @abc.abstractmethod
    def detail(self, id: int) -> Optional[model.Rental]:
        raise NotImplementedError()

    @abc.abstractmethod
    def detail2(self, id: int) -> Optional[domain_model.Rental]:
        raise NotImplementedError()

    @abc.abstractmethod
    def create(self, rental: model.Rental) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def create2(self, rental: domain_model.Rental) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, rental: model.Rental) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def update2(self, rental: domain_model.Rental) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self) -> None:
        raise NotImplementedError()
