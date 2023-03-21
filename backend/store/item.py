from typing import Optional

from sqlalchemy import or_
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from domain import Item
from model import ItemDTO, RentalDTO
from repository import ItemStoreInterface
from schema import PaginationQuery
from store.util import pagination_query
from util.logging import get_logger

logger = get_logger()


class ItemStore(ItemStoreInterface):
    def __init__(self, session: Session) -> None:
        self.db = session

    def list_public(self, pagination: PaginationQuery, isAvailable: bool) -> list[Item]:
        try:
            query = self.db.query(ItemDTO).filter(ItemDTO.available == True)  # NOQA

            # 未予約のものだけに絞り込む (未予約=予約record無しor返却されている)
            if isAvailable:
                sub_query = self.db.query(RentalDTO).filter(
                    RentalDTO.returned_date == None  # NOQA
                )
                query = query.join(
                    RentalDTO, ItemDTO.id == RentalDTO.item_id, isouter=True
                ).filter(
                    or_(RentalDTO.id == None, ~sub_query.exists())  # NOQA
                )

            items: list[ItemDTO] = pagination_query(
                ItemDTO, query, pagination, ItemDTO.id
            )
            return self.__convert_to_domain_model_list(items)
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def list_by_user_id(self, pagination: PaginationQuery, user_id: int) -> list[Item]:
        try:
            query = self.db.query(ItemDTO).filter(ItemDTO.owner_id == user_id)
            items: list[ItemDTO] = pagination_query(
                ItemDTO, query, pagination, ItemDTO.id
            )
            return self.__convert_to_domain_model_list(items)
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def detail(self, id: int) -> Optional[Item]:
        try:
            item: ItemDTO = self.db.query(ItemDTO).filter(ItemDTO.id == id).one()
            return item.to_domain_model()
        except NoResultFound as err:
            logger.info(f"({__name__}): {err}")
            return None
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def create(self, domain_item: Item) -> None:
        try:
            item: ItemDTO = ItemDTO.from_domain_model(domain_item)
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
        items: list[ItemDTO],
    ) -> list[Item]:
        domain_items: list[Item] = []
        for item in items:
            domain_items.append(item.to_domain_model())
        return domain_items
