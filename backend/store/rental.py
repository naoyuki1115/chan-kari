import abc

import model
from sqlalchemy.orm import Session
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
    def detail(self) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def create(self, rental: model.Rental) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self) -> None:
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

    def detail(self) -> None:
        raise NotImplementedError()

    def create(self, rental: model.Rental) -> None:
        try:
            self.db.add(rental)
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def update(self) -> None:
        raise NotImplementedError()

    def delete(self) -> None:
        raise NotImplementedError()
