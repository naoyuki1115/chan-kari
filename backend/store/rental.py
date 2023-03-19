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

    def list_valid(self) -> list[domain_model.Rental]:
        try:
            rentals: list[model.Rental] = (
                self.db.query(model.Rental)
                .filter(model.Rental.returned_date == None)  # NOQA
                .order_by(model.Rental.id)
                .all()
            )
            return self.__convert_to_domain_model_list(rentals)
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def list_by_user_id(
        self,
        user_id: int,
        closed: bool,
        pagination: PaginationQuery,
    ) -> list[domain_model.Rental]:
        try:
            query = self.db.query(model.Rental).filter(model.Rental.user_id == user_id)
            if closed is True:
                query = query.filter(model.Rental.returned_date != None)  # NOQA
            else:
                query = query.filter(model.Rental.returned_date == None)  # NOQA
            rentals: list[model.Rental] = pagination_query(
                model.Rental, query, pagination, model.Rental.id
            )
            return self.__convert_to_domain_model_list(rentals)
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def detail(self, id: int) -> Optional[domain_model.Rental]:
        try:
            rental = self.db.query(model.Rental).filter(model.Rental.id == id).one()
            return domain_model.Rental.to_domain_model(rental)
        except NoResultFound as err:
            logger.info(f"({__name__}): {err}")
            return None
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def create(self, domain_rental: domain_model.Rental) -> None:
        try:
            rental = model.Rental.from_domain_model(domain_rental)
            self.db.add(rental)
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def update(self, domain_rental: domain_model.Rental) -> None:
        try:
            rental: model.Rental = (
                self.db.query(model.Rental)
                .filter(model.Rental.id == domain_rental.get_id())
                .one()
            )
            rental.user_id = domain_rental.get_user_id()
            rental.item_id = domain_rental.get_item().get_id()
            rental.rented_date = domain_rental.get_rented_date()
            rental.return_plan_date = domain_rental.get_return_plan_date()
            rental.returned_date = domain_rental.get_returned_date()
        except NoResultFound as err:
            logger.error(f"({__name__}): {err}")
            return None
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def delete(self) -> None:
        raise NotImplementedError()

    def __convert_to_domain_model_list(
        self,
        rentals: list[model.Rental],
    ) -> list[domain_model.Rental]:
        domain_rentals: list[domain_model.Rental] = []
        for rental in rentals:
            domain_rentals.append(domain_model.Rental.to_domain_model(rental))
        return domain_rentals
