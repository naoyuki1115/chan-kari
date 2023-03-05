import abc

import domain_model
import model
from database.transaction import TransactionInterface
from psycopg2.errors import ForeignKeyViolation
from repository import ItemStoreInterface, RentalStoreInterface
from schema import (
    ItemCreateRequest,
    ItemCreateResponse,
    ItemListParams,
    ItemResponse,
    ItemStatus,
    PaginationQuery,
)
from util.error_msg import NotFoundError
from util.logging import get_logger

logger = get_logger()


class ItemUseCaseInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_list(
        self, pagination: PaginationQuery, params: ItemListParams
    ) -> list[ItemResponse]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_my_list(
        self, pagination: PaginationQuery, user_id: int
    ) -> list[ItemResponse]:
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

    def get_list(
        self, pagination: PaginationQuery, params: ItemListParams
    ) -> list[ItemResponse]:
        try:
            items: list[model.Item] = self.item_store.list_available(pagination)
            valid_rentals: list[model.Rental] = self.rental_store.list_valid()

            item_res_list: list[ItemResponse] = []
            for item in items:
                if not item.available:
                    continue
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
            if bool(params.available):
                return list(
                    filter(lambda i: i.status == ItemStatus.available, item_res_list)
                )
            return item_res_list
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def get_list2(
        self, pagination: PaginationQuery, params: ItemListParams
    ) -> list[domain_model.Item]:
        try:
            return self.item_store.list_public(pagination, bool(params.available))
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def get_my_list(
        self, pagination: PaginationQuery, user_id: int
    ) -> list[ItemResponse]:
        try:
            items: list[model.Item] = self.item_store.list_by_user_id(
                pagination, user_id
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
            return item_res_list
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def get_my_list2(
        self, pagination: PaginationQuery, user_id: int
    ) -> list[domain_model.Item]:
        try:
            return self.item_store.list_by_user_id2(pagination, user_id)
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def create_item(self, req: ItemCreateRequest, user_id: int) -> ItemCreateResponse:
        try:
            item = model.Item(
                name=req.name,
                owner_id=user_id,
                available=not req.draft,
                image_url=req.image_url,
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

    def create_item2(self, req: ItemCreateRequest, user_id: int) -> domain_model.Item:
        try:
            item = domain_model.Item(
                req.name, user_id, req.image_url, req.description, req.author
            )
            item.set_public_status()
            self.item_store.create2(item)
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
