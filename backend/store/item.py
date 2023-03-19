from typing import Optional

import domain_model
import model
from repository import ItemStoreInterface
from schema import PaginationQuery
from sqlalchemy import or_
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from store.util import pagination_query
from util.logging import get_logger

logger = get_logger()


class ItemStore(ItemStoreInterface):
    def __init__(self, session: Session) -> None:
        self.db = session

    def list_available(self, pagination: PaginationQuery) -> list[model.Item]:
        try:
            q = self.db.query(model.Item).filter(model.Item.available == True)  # NOQA
            return pagination_query(model.Item, q, pagination, model.Item.id)
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def list_public(
        self, pagination: PaginationQuery, isAvailable: bool
    ) -> list[domain_model.Item]:
        try:
            query = (
                self.db.query(model.Item)
                .join(model.Item.id == model.Rental.item_id, isouter=True)
                .filter(model.Item.available == True)  # NOQA
            )
            # 未予約のものだけに絞り込む (未予約=予約record無しor返却されている)
            if isAvailable:
                query = query.filter(
                    or_(
                        model.Rental == None,  # NOQA
                        model.Rental.returned_date != None,  # NOQA
                    )
                )
            items_with_rental: list[model.Item] = pagination_query(
                model.Item, query, pagination, model.Item.id
            )

            domain_items: list[domain_model.Item] = []
            for item_with_rental in items_with_rental:
                domain_item = domain_model.Item.to_domain_model(item_with_rental)
                if domain_item.get_status == domain_model.ItemStatus.private:
                    raise
                domain_items.append(domain_item)
            return domain_items
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def list_by_user_id(
        self, pagination: PaginationQuery, user_id: int
    ) -> list[model.Item]:
        try:
            q = self.db.query(model.Item).filter(model.Item.owner_id == user_id)
            return pagination_query(model.Item, q, pagination, model.Item.id)
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def list_by_user_id2(
        self, pagination: PaginationQuery, user_id: int
    ) -> list[domain_model.Item]:
        try:
            query = self.db.query(model.Item).filter(model.Item.owner_id == user_id)
            items: list[model.Item] = pagination_query(
                model.Item, query, pagination, model.Item.id
            )
            domain_items: list[domain_model.Item] = []
            for item in items:
                domain_items.append(domain_model.Item.to_domain_model(item))
            return domain_items
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def list(self) -> list[model.Item]:
        raise NotImplementedError()

    def detail(self, id: int) -> Optional[model.Item]:
        try:
            return self.db.query(model.Item).filter(model.Item.id == id).one()
        except NoResultFound as err:
            logger.error(f"({__name__}): {err}")
            return None
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def create(self, item: model.Item) -> None:
        try:
            self.db.add(item)
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def update(self) -> None:
        raise NotImplementedError()

    def delete(self) -> None:
        raise NotImplementedError()
