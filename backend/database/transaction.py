import abc

from sqlalchemy.orm import Session


class TransactionInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def begin(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError()


class Transaction(TransactionInterface):
    def __init__(self, session: Session) -> None:
        self.db = session

    def begin(self):
        self.db.begin()

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()
