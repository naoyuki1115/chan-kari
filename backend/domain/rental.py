from datetime import date, datetime
from enum import Enum
from typing import Optional
from zoneinfo import ZoneInfo

from domain import Item, ItemStatus
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
    __item: Item
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

    def set_id(self, id: int):
        self.__id = id

    def set_returned_date(self, return_date: date):
        self.__returned_date = return_date

    def __init__(
        self,
        user_id: int,
        item: Item,
        rented_date: date,
        return_plan_date: date,
    ):
        self.__user_id = user_id
        self.__item = item
        self.__rented_date = rented_date
        self.__return_plan_date = return_plan_date
        self.set_status()

    @classmethod
    def new_rental(
        cls,
        user_id: int,
        item: Optional[Item],
        rented_date: date,
        return_plan_date: date,
    ) -> "Rental":
        if item is None or item.get_id() is None:
            raise NotFoundError
        if item.get_owner_id() == user_id:
            raise OperationIsForbiddenError
        if item.get_status() == ItemStatus.private:
            raise ResourceUnavailableError
        elif item.get_status() == ItemStatus.rented:
            raise ResourceAlreadyExistsError
        return cls(user_id, item, rented_date, return_plan_date)

    def return_item(self, user_id: int):
        if self.__user_id != user_id:
            raise OperationIsForbiddenError
        if self.__returned_date is not None:
            raise ResourceAlreadyExistsError

        self.__status = RentalStatus.returned
        self.__returned_date = datetime.now(ZoneInfo("Asia/Tokyo")).date()
