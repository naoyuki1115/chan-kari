import abc

import model
from database.transaction import TransactionInterface
from psycopg2.errors import ForeignKeyViolation
from schema import (
    ItemCreateRequest,
    ItemCreateResponse,
    ItemListRequest,
    ItemResponse,
    ItemStatus,
)
from store import ItemStoreInterface, RentalStoreInterface
from util.error_msg import NotFoundError
from util.logging import get_logger

logger = get_logger()


class ItemUseCaseInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_list(self, req: ItemListRequest) -> list[ItemResponse]:
        raise NotImplementedError

    @abc.abstractmethod
    def create_item(self, req: ItemCreateRequest, user_id: int) -> ItemCreateResponse:
        raise NotImplementedError


class ItemUseCase(ItemUseCaseInterface):
    def __init__(
        self,
        tx: TransactionInterface,
        item: ItemStoreInterface,
        rental: RentalStoreInterface,
    ):
        self.tx: TransactionInterface = tx
        self.item_store: ItemStoreInterface = item
        self.rental_store: RentalStoreInterface = rental

    def get_list(self, req: ItemListRequest) -> list[ItemResponse]:
        try:
            items: list[model.Item] = self.item_store.list_available(
                req.limit, req.after, req.before
            )
            valid_rentals: list[model.Rental] = self.rental_store.list_valid()

            item_res_list: list[ItemResponse] = []
            for item in items:
                if not item.available:
                    status: ItemStatus = ItemStatus.unavailable
                elif (
                    len(list(filter(lambda r: r.item_id == item.id, valid_rentals)))
                    != 0
                ):
                    status: ItemStatus = ItemStatus.rented
                else:
                    status: ItemStatus = ItemStatus.available
                item_res_list.append(
                    ItemResponse.new(item.id, item.name, status, item.image_url)
                )
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

        if bool(req.available):
            return list(
                filter(lambda i: i.status == ItemStatus.available, item_res_list)
            )

        return item_res_list

    def create_item(self, req: ItemCreateRequest, user_id: int) -> ItemCreateResponse:
        try:
            item = model.Item(
                name=req.name,
                owner_id=user_id,
                available=not req.draft,
                image_url=req.imageUrl,
                description=req.description,
                author=req.author,
            )
            self.item_store.create(item)
            self.tx.commit()
            return ItemCreateResponse.new(item.id)
        except ForeignKeyViolation as err:
            logger.error(f"({__name__}): {err}")
            self.tx.rollback()
            raise NotFoundError
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            self.tx.rollback()
            raise
