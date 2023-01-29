from fastapi import APIRouter, Depends
from schema.item import ItemListRequest, ItemResponse, Status

router = APIRouter(
    prefix="/items",
)


@router.get("")
def list(req: ItemListRequest = Depends()) -> list[ItemResponse]:
    return [
        ItemResponse(id=req.limit, status=Status["rented"], name="test", imageUrl=None)
    ]
