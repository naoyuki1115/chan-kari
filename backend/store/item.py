import abc
from typing import Optional

import model
from schema import PaginationQuery
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from store.util import pagination_query
from util.logging import get_logger

logger = get_logger()


class ItemStoreInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def list_available(self, pagination: PaginationQuery) -> list[model.Item]:
        raise NotImplementedError()

    @abc.abstractmethod
    def list_by_user_id(
        self, pagination: PaginationQuery, user_id: int
    ) -> list[model.Item]:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(self) -> list[model.Item]:
        raise NotImplementedError()

    @abc.abstractmethod
    def detail(self, id: int) -> Optional[model.Item]:
        raise NotImplementedError()

    @abc.abstractmethod
    def create(self, item: model.Item) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self) -> None:
        raise NotImplementedError()


class ItemStore(ItemStoreInterface):
    def __init__(self, session: Session) -> None:
        self.db = session

    def list_available(self, pagination: PaginationQuery) -> list[model.Item]:
        try:
            q = self.db.query(model.Item).filter(model.Item.available == True)  # NOQA
            return pagination_query(model.Item, q, pagination, model.Item.id)
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def list(self) -> list[model.Item]:
        raise NotImplementedError()

    def detail(self, id: int) -> Optional[model.Item]:
        try:
            return self.db.query(model.Item).filter(model.Item.id == id).one()
        except NoResultFound as err:
            logger.error(f"({__name__}): {err}")
            return None
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def create(self, item: model.Item) -> None:
        try:
            self.db.add(item)
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def update(self) -> None:
        raise NotImplementedError()

    def delete(self) -> None:
        raise NotImplementedError()
