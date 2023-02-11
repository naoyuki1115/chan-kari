import abc

import model
from database.transaction import TransactionInterface
from psycopg2.errors import ForeignKeyViolation, UniqueViolation
from schema import RentRequest, RentResponse
from store import ItemStoreInterface, RentalStoreInterface
from util.error_msg import (
    NotFoundError,
    OperationIsForbiddenError,
    ResourceAlreadyExistsError,
    ResourceUnavailableError,
)
from util.logging import get_logger

logger = get_logger()


class RentalUseCaseInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_rental(self, req: RentRequest, user_id: int) -> RentResponse:
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

    def create_rental(self, req: RentRequest, user_id: int) -> RentResponse:
        try:
            item: model.Item = self.item_store.detail(req.itemId)
            if item is None:
                raise NotFoundError
            if item.owner_id == user_id:
                raise OperationIsForbiddenError
            if item.available is False:
                raise ResourceUnavailableError

            rental = model.Rental(
                user_id=user_id,
                item_id=req.itemId,
                rented_date=req.rentalDate,
                return_plan_date=req.returnPlanDate,
            )
            self.rental_store.create(rental)
            self.tx.commit()
            return RentResponse.new(rental.id)
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
