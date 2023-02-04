from database.database import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from schema import ItemListRequest, ItemResponse
from sqlalchemy.orm import Session
from store import ItemStore, ItemStoreInterface, RentalStore, RentalStoreInterface
from usecase import ItemUseCase, ItemUseCaseInterface
from util.logging import get_logger

router = APIRouter(
    prefix="/items",
)


def new_item_usecase(db: Session = Depends(get_db)) -> ItemUseCaseInterface:
    item_store: ItemStoreInterface = ItemStore(db)
    renal_store: RentalStoreInterface = RentalStore(db)
    return ItemUseCase(item_store, renal_store)


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
    except Exception as e:
        get_logger(__name__).error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    return items
