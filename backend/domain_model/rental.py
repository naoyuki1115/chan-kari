from datetime import date, datetime
from enum import Enum
from typing import Optional
from zoneinfo import ZoneInfo

import domain_model
import model
from domain_model.item import ItemStatus
from util.error_msg import (
    NotFoundError,
    OperationIsForbiddenError,
    ResourceAlreadyExistsError,
    ResourceUnavailableError,
)


class RentalStatus(str, Enum):
    active = "active"
    returned = "returned"
    overdue = "overdue"


class Rental:
    __id: int
    __user_id: int
    __item: domain_model.Item
    __status: RentalStatus
    __rented_date: date
    __return_plan_date: date
    __returned_date: Optional[date] = None

    # getter
    def get_id(self):
        return self.__id

    def get_user_id(self):
        return self.__user_id

    def get_item(self):
        return self.__item

    def get_status(self):
        return self.__status

    def get_rented_date(self):
        return self.__rented_date

    def get_return_plan_date(self):
        return self.__return_plan_date

    def get_returned_date(self):
        return self.__returned_date

    def set_status(self):
        if self.get_returned_date() is not None:
            self.__status = RentalStatus.returned
        elif self.get_return_plan_date() < datetime.now(ZoneInfo("Asia/Tokyo")).date():
            self.__status = RentalStatus.overdue
        else:
            self.__status = RentalStatus.active

    def __init__(
        self,
        user_id: int,
        item: Optional[domain_model.Item],
        rented_date: date,
        return_plan_date: date,
    ):
        if item is None or item.get_id() is None:
            raise NotFoundError
        if item.get_owner_id() == user_id:
            raise OperationIsForbiddenError
        if item.get_status() == ItemStatus.public:
            raise ResourceUnavailableError

        self.__user_id = user_id
        self.__item = item
        self.__rented_date: date = rented_date
        self.__return_plan_date: date = return_plan_date
        self.set_status()

    def return_item(self, user_id: int):
        if self.__user_id != user_id:
            raise OperationIsForbiddenError
        if self.__returned_date is not None:
            raise ResourceAlreadyExistsError

        self.__status = RentalStatus.returned
        self.__returned_date = datetime.now(ZoneInfo("Asia/Tokyo")).date()

    @classmethod
    def to_domain_model(cls, rental: model.Rental):
        model = cls(
            user_id=rental.user_id,
            item=rental.item,
            rented_date=rental.rented_date,
            return_plan_date=rental.return_plan_date,
        )
        model.__id = rental.id
        model.__returned_date = rental.returned_date
        model.set_status()
        return model
