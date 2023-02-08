import abc

import model
from sqlalchemy.orm import Session


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
    def create(self) -> None:
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
        return (
            self.db.query(model.Rental)
            .filter(model.Rental.returned_at == None)  # NOQA
            .order_by(model.Rental.id)
            .all()
        )

    def list(self) -> None:
        raise NotImplementedError()

    def detail(self) -> None:
        raise NotImplementedError()

    def create(self) -> None:
        raise NotImplementedError()

    def update(self) -> None:
        raise NotImplementedError()

    def delete(self) -> None:
        raise NotImplementedError()
