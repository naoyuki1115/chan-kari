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
            items: list[model.Item] = pagination_query(
                model.Item, query, pagination, model.Item.id
            )
            return self.__convert_to_domain_model_list(items)
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def list_by_user_id(
        self, pagination: PaginationQuery, user_id: int
    ) -> list[domain_model.Item]:
        try:
            query = self.db.query(model.Item).filter(model.Item.owner_id == user_id)
            items: list[model.Item] = pagination_query(
                model.Item, query, pagination, model.Item.id
            )
            return self.__convert_to_domain_model_list(items)
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def detail(self, id: int) -> Optional[domain_model.Item]:
        try:
            item: model.Item = (
                self.db.query(model.Item).filter(model.Item.id == id).one()
            )
            return domain_model.Item.to_domain_model(item)
        except NoResultFound as err:
            logger.info(f"({__name__}): {err}")
            return None
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def create(self, domain_item: domain_model.Item) -> None:
        try:
            item: model.Item = model.Item.from_domain_model(domain_item)
            self.db.add(item)
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def update(self) -> None:
        raise NotImplementedError()

    def delete(self) -> None:
        raise NotImplementedError()

    def __convert_to_domain_model_list(
        self,
        items: list[model.Item],
    ) -> list[domain_model.Item]:
        domain_items: list[domain_model.Item] = []
        for item in items:
            domain_items.append(domain_model.Item.to_domain_model(item))
        return domain_items
