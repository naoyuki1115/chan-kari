from fastapi import APIRouter, status

router = APIRouter(
    prefix="/rentals",
)


@router.get("")
def list_rental():
    return [
        {
            "id": 1,
            "closed": False,
            "rental_date": "2022-06-06",
            "return_plan_date": "2022-06-06",
            "return_date": "2022-06-06",
            "itemId": 1,
            "itemName": "item name",
        }
    ]


@router.get("/{item_id}")
def get_rental(item_id: int):
    return [
        {
            "itemId": item_id,
            "rental_date": "2022-06-06",
            "return_plan_date": "2022-06-06",
        }
    ]


@router.post("")
def rental():
    return [{"id": 1}]


@router.put("/{rental_id}/return", status_code=status.HTTP_204_NO_CONTENT)
def return_rental():
    pass
