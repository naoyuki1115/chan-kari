import abc

import model
from database.transaction import TransactionInterface
from schema import RentRequest, RentResponse
from store import ItemStoreInterface, RentalStoreInterface
from util.error_msg import (
    NotFoundError,
    OperationIsForbiddenError,
    ResourceUnavailableError,
)


class RentalUseCaseInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_rental(self, req: RentRequest, user_id: int) -> list[RentResponse]:
        raise NotImplementedError


class RentalUseCase(RentalUseCaseInterface):
    def __init__(
        self,
        tx: TransactionInterface,
        rental: RentalStoreInterface,
        item: ItemStoreInterface,
    ):
        self.tx: TransactionInterface = tx
        self.rental_store: RentalStoreInterface = rental
        self.item_store: ItemStoreInterface = item

    def create_rental(self, req: RentRequest, user_id: int) -> list[RentResponse]:
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
        except Exception:
            self.tx.rollback()
            raise
        return rental
