import abc
from typing import Optional

import model
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from util.logging import get_logger

logger = get_logger()


class RentalStoreInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def list_valid(self) -> list[model.Rental]:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(self) -> None:
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


class RentalStore(RentalStoreInterface):
    def __init__(self, session: Session) -> None:
        self.db = session

    def list_valid(self) -> list[model.Rental]:
        try:
            return (
                self.db.query(model.Rental)
                .filter(model.Rental.returned_date == None)  # NOQA
                .order_by(model.Rental.id)
                .all()
            )
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def list(self) -> None:
        raise NotImplementedError()

    def detail(self, id: int) -> Optional[model.Rental]:
        try:
            return self.db.query(model.Rental).filter(model.Rental.id == id).one()
        except NoResultFound as err:
            logger.error(f"({__name__}): {err}")
            return None
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def create(self, rental: model.Rental) -> None:
        try:
            self.db.add(rental)
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def update(self, rental: model.Rental) -> None:
        try:
            _rental: model.Rental = (
                self.db.query(model.Rental).filter(model.Rental.id == rental.id).one()
            )
            _rental.user_id = rental.user_id
            _rental.item_id = rental.item_id
            _rental.rented_date = rental.rented_date
            _rental.returned_date = rental.returned_date
            _rental.return_plan_date = rental.return_plan_date
        except NoResultFound as err:
            logger.error(f"({__name__}): {err}")
            return None
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def delete(self) -> None:
        raise NotImplementedError()
