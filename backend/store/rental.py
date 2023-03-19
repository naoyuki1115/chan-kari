from typing import Optional

import domain_model
import model
from repository import RentalStoreInterface
from schema import PaginationQuery
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from store.util import pagination_query
from util.logging import get_logger

logger = get_logger()


class RentalStore(RentalStoreInterface):
    def __init__(self, session: Session) -> None:
        self.db = session

    def list_valid(self) -> list[model.Rental]:
        try:
            return (
                self.db.query(model.Rental)
                .filter(model.Rental.returned_date == None)  # NOQA
                .order_by(model.Rental.id)
                .all()
            )
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def list_by_user_id(
        self,
        user_id: int,
        closed: bool,
        pagination: PaginationQuery,
    ) -> list[model.Rental]:
        try:
            q = self.db.query(model.Rental).filter(model.Rental.user_id == user_id)
            if closed is False:
                q = q.filter(model.Rental.returned_date == None)  # NOQA
            return pagination_query(model.Rental, q, pagination, model.Rental.id)
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def list(self) -> list[model.Rental]:
        raise NotImplementedError()

    def detail(self, id: int) -> Optional[model.Rental]:
        try:
            return self.db.query(model.Rental).filter(model.Rental.id == id).one()
        except NoResultFound as err:
            logger.error(f"({__name__}): {err}")
            return None
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def detail2(self, id: int) -> Optional[domain_model.Rental]:
        try:
            rental = self.db.query(model.Rental).filter(model.Rental.id == id).one()
            return domain_model.Rental.to_domain_model(rental)
        except NoResultFound as err:
            logger.info(f"({__name__}): {err}")
            return None
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def create(self, rental: model.Rental) -> None:
        try:
            self.db.add(rental)
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def create2(self, domain_rental: domain_model.Rental) -> None:
        try:
            rental = model.Rental.from_domain_model(domain_rental)
            self.db.add(rental)
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def update(self, rental: model.Rental) -> None:
        try:
            _rental: model.Rental = (
                self.db.query(model.Rental).filter(model.Rental.id == rental.id).one()
            )
            _rental.user_id = rental.user_id
            _rental.item_id = rental.item_id
            _rental.rented_date = rental.rented_date
            _rental.returned_date = rental.returned_date
            _rental.return_plan_date = rental.return_plan_date
        except NoResultFound as err:
            logger.error(f"({__name__}): {err}")
            return None
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def delete(self) -> None:
        raise NotImplementedError()
