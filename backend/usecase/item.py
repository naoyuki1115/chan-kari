import abc

from psycopg2.errors import ForeignKeyViolation

from database.transaction import TransactionInterface
from domain import Item
from repository import ItemStoreInterface, RentalStoreInterface
from schema import ItemCreateRequest, ItemListParams, PaginationQuery
from util.error_msg import NotFoundError
from util.logging import get_logger

logger = get_logger()


class ItemUseCaseInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_list(
        self, pagination: PaginationQuery, params: ItemListParams
    ) -> list[Item]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_my_list(self, pagination: PaginationQuery, user_id: int) -> list[Item]:
        raise NotImplementedError

    @abc.abstractmethod
    def create_item(self, req: ItemCreateRequest, user_id: int) -> Item:
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

    def get_list(
        self, pagination: PaginationQuery, params: ItemListParams
    ) -> list[Item]:
        try:
            return self.item_store.list_public(pagination, bool(params.available))
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def get_my_list(self, pagination: PaginationQuery, user_id: int) -> list[Item]:
        try:
            return self.item_store.list_by_user_id(pagination, user_id)
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def create_item(self, req: ItemCreateRequest, user_id: int) -> Item:
        try:
            item: Item = Item(
                req.name, user_id, req.image_url, req.description, req.author
            )
            if req.draft:
                item.set_private_status()
            else:
                item.set_public_status()
            self.item_store.create(item)
            self.tx.commit()
            return item
        except ForeignKeyViolation as err:
            logger.error(f"({__name__}): {err}")
            self.tx.rollback()
            raise NotFoundError
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            self.tx.rollback()
            raise
