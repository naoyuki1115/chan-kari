import abc

import model
from schema import ItemListRequest, ItemResponse, ItemStatus
from store import ItemStore, RentalStore


class ItemUseCaseInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_list(
        self,
        req: ItemListRequest,
    ) -> list[ItemResponse]:
        raise NotImplementedError


class ItemUseCase(ItemUseCaseInterface):
    def __init__(self, item: ItemStore, rental: RentalStore):
        self.item_store: ItemStore = item
        self.rental_store: RentalStore = rental

    def get_list(
        self,
        req: ItemListRequest,
    ) -> list[ItemResponse]:
        items: list[model.Item] = self.item_store.list_available(
            req.limit, req.after, req.before
        )
        not_returned_rentals: list[model.Rental] = self.rental_store.list_not_returned()

        item_res_list: list[ItemResponse] = []
        for item in items:
            if not item.available:
                status: ItemStatus = ItemStatus.unavailable
            elif (
                len(list(filter(lambda r: r.item_id == item.id, not_returned_rentals)))
                != 0
            ):
                status: ItemStatus = ItemStatus.rented
            else:
                status: ItemStatus = ItemStatus.available
            item_res_list.append(
                ItemResponse.new(item.id, item.name, status, item.image_url)
            )

        if bool(req.available):
            return list(
                filter(lambda i: i.status == ItemStatus.available, item_res_list)
            )

        return item_res_list
