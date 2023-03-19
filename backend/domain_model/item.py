from enum import Enum
from typing import Optional

import model


class ItemStatus(str, Enum):
    public = "public"
    private = "private"
    rented = "rented"


class Item:
    __id: int
    __name: str
    __owner_id: int
    __status: ItemStatus
    __image_url: Optional[str] = None
    __description: Optional[str] = None
    __author: Optional[str] = None

    # getter
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_owner_id(self):
        return self.__owner_id

    def get_status(self):
        return self.__status

    def get_image_url(self):
        return self.__image_url

    def get_description(self):
        return self.__description

    def get_author(self):
        return self.__author

    def __init__(
        self,
        name: str,
        owner_id: int,
        image_url: Optional[str],
        description: Optional[str],
        author: Optional[str],
    ):
        self.__name = name
        self.__owner_id = owner_id
        self.__status = ItemStatus.private
        self.__image_url = image_url
        self.__description = description
        self.__author = author

    def set_public_status(self):
        self.__status = ItemStatus.public

    def set_private_status(self):
        self.__status = ItemStatus.private

    def set_rented_status(self):
        self.__status = ItemStatus.rented

    def __judge_status(self, item_with_rental: model.Item):
        if item_with_rental.available is False:
            self.__status = ItemStatus.private
        elif (
            len(list(filter(lambda r: r.returned_date is None, item_with_rental.rentals)))
            > 0
        ):
            self.__status = ItemStatus.rented
        else:
            self.__status = ItemStatus.public

    @classmethod
    def to_domain_model(cls, item_with_rental: model.Item):
        model = cls(
            name=item_with_rental.name,
            owner_id=item_with_rental.owner_id,
            image_url=item_with_rental.image_url,
            description=item_with_rental.description,
            author=item_with_rental.author,
        )
        model.__id = item_with_rental.id
        model.__judge_status(item_with_rental)
        return model
