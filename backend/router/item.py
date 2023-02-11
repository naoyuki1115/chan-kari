from database.database import get_db
from database.transaction import Transaction, TransactionInterface
from fastapi import APIRouter, Depends, HTTPException, status
from schema import ItemListRequest, ItemResponse
from sqlalchemy.orm import Session
from store import ItemStore, ItemStoreInterface, RentalStore, RentalStoreInterface
from usecase import ItemUseCase, ItemUseCaseInterface
from util.logging import get_logger

router = APIRouter(
    prefix="/items",
)

logger = get_logger()


def new_item_usecase(db: Session = Depends(get_db)) -> ItemUseCaseInterface:
    tx: TransactionInterface = Transaction(db)
    item_store: ItemStoreInterface = ItemStore(db)
    renal_store: RentalStoreInterface = RentalStore(db)
    return ItemUseCase(tx, item_store, renal_store)


@router.get("", response_model=list[ItemResponse])
def list_item(
    req: ItemListRequest = Depends(),
    item_usecase: ItemUseCaseInterface = Depends(new_item_usecase),
) -> list[ItemResponse]:
    if req.after is not None and req.before is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only either `before` or `after` can be specified",
        )
    try:
        items = item_usecase.get_list(req)
    except Exception as err:
        logger.error(f"({__name__}): {err}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    return items


@router.get("/{item_id}")
def item(item_id: int):
    return {
        "id": item_id,
        "name": "item name",
        "status": "available",
        "imageUrl": "http://example.com/test.png",
        "description": "description",
        "author": "author",
        "ownerId": 1,
        "ownerNickName": "nick name",
    }
