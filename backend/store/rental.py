from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from domain import Rental
from model import RentalDTO
from repository import RentalStoreInterface
from schema import PaginationQuery
from store.util import pagination_query
from util.logging import get_logger

logger = get_logger()


class RentalStore(RentalStoreInterface):
    def __init__(self, session: Session) -> None:
        self.db = session

    def list_valid(self) -> list[Rental]:
        try:
            rentals: list[RentalDTO] = (
                self.db.query(RentalDTO)
                .filter(RentalDTO.returned_date == None)  # NOQA
                .order_by(RentalDTO.id)
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
    ) -> list[Rental]:
        try:
            query = self.db.query(RentalDTO).filter(RentalDTO.user_id == user_id)
            if closed is True:
                query = query.filter(RentalDTO.returned_date != None)  # NOQA
            else:
                query = query.filter(RentalDTO.returned_date == None)  # NOQA
            rentals: list[RentalDTO] = pagination_query(
                RentalDTO, query, pagination, RentalDTO.id
            )
            return self.__convert_to_domain_model_list(rentals)
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def detail(self, id: int) -> Optional[Rental]:
        try:
            rental: RentalDTO = (
                self.db.query(RentalDTO).filter(RentalDTO.id == id).one()
            )
            return rental.to_domain_model()
        except NoResultFound as err:
            logger.info(f"({__name__}): {err}")
            return None
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def create(self, domain_rental: Rental) -> None:
        try:
            rental = RentalDTO.from_domain_model(domain_rental)
            self.db.add(rental)
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise

    def update(self, domain_rental: Rental) -> None:
        try:
            rental: RentalDTO = (
                self.db.query(RentalDTO)
                .filter(RentalDTO.id == domain_rental.get_id())
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
        rentals: list[RentalDTO],
    ) -> list[Rental]:
        domain_rentals: list[Rental] = []
        for rental in rentals:
            domain_rentals.append(rental.to_domain_model())
        return domain_rentals
