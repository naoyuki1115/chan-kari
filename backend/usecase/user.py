import abc
from typing import Optional

from database.transaction import TransactionInterface
from domain import User
from repository import UserStoreInterface
from util.logging import get_logger

logger = get_logger()


class UserUseCaseInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_user(
        self,
        uid: str,
        name: str,
        email: str,
        image_url: Optional[str] = None,
    ) -> None:
        raise NotImplementedError


class UserUseCase(UserUseCaseInterface):
    def __init__(
        self,
        tx: TransactionInterface,
        user: UserStoreInterface,
    ):
        self.tx: TransactionInterface = tx
        self.user_store: UserStoreInterface = user

    def create_user(
        self,
        uid: str,
        name: str,
        email: str,
        image_url: Optional[str] = None,
    ) -> None:
        try:
            user = User(
                uid=uid,
                name=name,
                email=email,
                image_url=image_url,
            )
            self.user_store.create(user)
            self.tx.commit()
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            self.tx.rollback()
            raise
