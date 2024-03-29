import abc

from database.transaction import TransactionInterface
from domain import Item
from repository import ItemStoreInterface, RentalStoreInterface
from schema import ItemCreateRequest, PaginationQuery
from util.logging import get_logger

logger = get_logger()


class ItemUseCaseInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_list(self, pagination: PaginationQuery, available: bool) -> list[Item]:
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

    def get_list(self, pagination: PaginationQuery, available: bool) -> list[Item]:
        try:
            return self.item_store.list_public(pagination, available)
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
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            self.tx.rollback()
            raise
