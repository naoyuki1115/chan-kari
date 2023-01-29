import model
import store.item
import store.rental
from schema.item import ItemResponse, ItemStatus
from sqlalchemy.orm import Session


def get_list(db: Session, rental_available: bool) -> list[ItemResponse]:
    items: list[model.Item] = store.item.list_available(db)
    valid_rentals: list[model.Rental] = store.rental.list_rented(db)

    item_res_list: list[ItemResponse] = []
    for item in items:
        if not item.available:
            status: ItemStatus = ItemStatus.unavailable
        elif len(list(filter(lambda r: r.item_id == item.id, valid_rentals))) != 0:
            status: ItemStatus = ItemStatus.rented
        else:
            status: ItemStatus = ItemStatus.available
        item_res_list.append(
            ItemResponse(
                id=item.id, name=item.name, status=status, imageUrl=item.image_url
            )
        )

    if rental_available:
        return list(filter(lambda i: i.status == ItemStatus.available, item_res_list))

    return item_res_list
