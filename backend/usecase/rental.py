import abc
from datetime import datetime
from zoneinfo import ZoneInfo

import model
from database.transaction import TransactionInterface
from psycopg2.errors import ForeignKeyViolation, UniqueViolation
from schema import (
    RentalListParams,
    RentalResponse,
    RentRequest,
    RentResponse,
    ReturnParams,
)
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
    def rent_item(self, req: RentRequest, user_id: int) -> RentResponse:
        raise NotImplementedError

    @abc.abstractmethod
    def return_item(self, params: ReturnParams, user_id: int) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def get_my_list(
        self, params: RentalListParams, user_id: int
    ) -> list[RentalResponse]:
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

    def rent_item(self, req: RentRequest, user_id: int) -> RentResponse:
        try:
            item: model.Item = self.item_store.detail(req.item_id)
            if item is None:
                raise NotFoundError
            if item.owner_id == user_id:
                raise OperationIsForbiddenError
            if item.available is False:
                raise ResourceUnavailableError

            rental = model.Rental(
                user_id=user_id,
                item_id=req.item_id,
                rented_date=req.rental_date,
                return_plan_date=req.return_plan_date,
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

    def return_item(self, params: ReturnParams, user_id: int) -> None:
        try:
            existing_rental = self.rental_store.detail(params.rental_id)
            if existing_rental is None:
                raise NotFoundError
            if existing_rental.user_id != user_id:
                raise OperationIsForbiddenError
            if existing_rental.returned_date is not None:
                raise ResourceAlreadyExistsError

            rental = model.Rental(
                id=existing_rental.id,
                user_id=existing_rental.user_id,
                item_id=existing_rental.item_id,
                rented_date=existing_rental.rented_date,
                return_plan_date=existing_rental.return_plan_date,
                returned_date=datetime.now(ZoneInfo("Asia/Tokyo")).date(),
            )
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
        self, params: RentalListParams, user_id: int
    ) -> list[RentalResponse]:
        raise NotImplementedError
