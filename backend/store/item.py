import abc
from typing import Optional

import model
from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound


class ItemStoreInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def list_available(
        self, limit: int, after: Optional[int], before: Optional[int]
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

    def list_available(
        self, limit: int, after: Optional[int], before: Optional[int]
    ) -> list[model.Item]:
        try:
            q = self.db.query(model.Item).filter(model.Item.available == True)  # NOQA
            if after is not None:
                return q.order_by(model.Item.id).offset(after).limit(limit).all()
            elif before is not None:
                items = (
                    q.order_by(desc(model.Item.id))
                    .filter(model.Item.id < before)
                    .limit(limit)
                    .all()
                )
                items.reverse()
                return items
            else:
                return q.order_by(model.Item.id).limit(limit).all()
        except Exception:
            raise

    def list(self) -> list[model.Item]:
        raise NotImplementedError()

    def detail(self, id: int) -> Optional[model.Item]:
        try:
            return self.db.query(model.Item).filter(model.Item.id == id).one()
        except NoResultFound:
            return None
        except Exception:
            raise

    def create(self, item: model.Item) -> None:
        try:
            self.db.add(item)
        except IntegrityError as err:
            raise err.orig
        except Exception:
            raise

    def update(self) -> None:
        raise NotImplementedError()

    def delete(self) -> None:
        raise NotImplementedError()
