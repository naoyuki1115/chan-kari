import abc
from typing import Optional

import domain_model
import model
from schema import PaginationQuery


class ItemStoreInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def list_available(self, pagination: PaginationQuery) -> list[model.Item]:
        raise NotImplementedError()

    @abc.abstractmethod
    def list_public(
        self, pagination: PaginationQuery, isAvailable: bool
    ) -> list[domain_model.Item]:
        raise NotImplementedError()

    @abc.abstractmethod
    def list_by_user_id(
        self, pagination: PaginationQuery, user_id: int
    ) -> list[model.Item]:
        raise NotImplementedError()

    @abc.abstractmethod
    def list_by_user_id2(
        self, pagination: PaginationQuery, user_id: int
    ) -> list[domain_model.Item]:
        raise NotImplementedError()

    @abc.abstractmethod
    def detail(self, id: int) -> Optional[model.Item]:
        raise NotImplementedError()

    @abc.abstractmethod
    def detail2(self, id: int) -> Optional[domain_model.Item]:
        raise NotImplementedError()

    @abc.abstractmethod
    def create(self, item: model.Item) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def create2(self, item: domain_model.Item) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self) -> None:
        raise NotImplementedError()
