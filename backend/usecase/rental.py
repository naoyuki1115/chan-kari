import abc
from typing import Optional

from psycopg2.errors import ForeignKeyViolation, UniqueViolation

from database.transaction import TransactionInterface
from domain import Rental
from repository import ItemStoreInterface, RentalStoreInterface
from schema import PaginationQuery, RentRequest
from util.error_msg import NotFoundError, ResourceAlreadyExistsError
from util.logging import get_logger

logger = get_logger()


class RentalUseCaseInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def rent_item(self, req: RentRequest, user_id: int) -> Rental:
        raise NotImplementedError

    @abc.abstractmethod
    def return_item(self, rental_id: int, user_id: int) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def get_my_list(
        self, pagination: PaginationQuery, closed: bool, user_id: int
    ) -> list[Rental]:
        raise NotImplementedError


class RentalUseCase(RentalUseCaseInterface):
    def __init__(
        self,
        tx: TransactionInterface,
        item: ItemStoreInterface,
        rental: RentalStoreInterface,
    ):
        self.tx: TransactionInterface = tx
        self.item_store: ItemStoreInterface = item
        self.rental_store: RentalStoreInterface = rental

    def rent_item(self, req: RentRequest, user_id: int) -> Rental:
        item = self.item_store.detail(req.item_id)
        rental = Rental(user_id, item, req.rental_date, req.return_plan_date)
        self.rental_store.create(rental)
        self.tx.commit()
        return rental

    def return_item(self, rental_id: int, user_id: int) -> None:
        try:
            rental: Optional[Rental] = self.rental_store.detail(rental_id)
            if rental is None:
                raise NotFoundError
            rental.return_item(user_id)
            self.rental_store.update(rental)
            self.tx.commit()
        except UniqueViolation as err:
            logger.error(f"({__name__}): {err}")
            self.tx.rollback()
            raise ResourceAlreadyExistsError
        except ForeignKeyViolation as err:
            logger.error(f"({__name__}): {err}")
            self.tx.rollback()
            raise NotFoundError
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            self.tx.rollback()
            raise

    def get_my_list(
        self, pagination: PaginationQuery, closed: bool, user_id: int
    ) -> list[Rental]:
        try:
            return self.rental_store.list_by_user_id(user_id, closed, pagination)
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise
