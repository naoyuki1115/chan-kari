from database.database import get_db
from database.transaction import Transaction, TransactionInterface
from fastapi import APIRouter, Depends, HTTPException, status
from schema import ItemCreateRequest, ItemCreateResponse, ItemResponse, PaginationQuery
from sqlalchemy.orm import Session
from store import ItemStore, RentalStore
from repository import ItemStoreInterface, RentalStoreInterface
from usecase import ItemUseCase, ItemUseCaseInterface
from util.error_msg import NotFoundError
from util.logging import get_logger

router = APIRouter()

logger = get_logger()


def new_item_usecase(db: Session = Depends(get_db)) -> ItemUseCaseInterface:
    tx: TransactionInterface = Transaction(db)
    item_store: ItemStoreInterface = ItemStore(db)
    renal_store: RentalStoreInterface = RentalStore(db)
    return ItemUseCase(tx, item_store, renal_store)


@router.post("", response_model=ItemCreateResponse)
def create_item(
    req: ItemCreateRequest,
    item_usecase: ItemUseCaseInterface = Depends(new_item_usecase),
) -> ItemCreateResponse:
    try:
        # TODO: headerのトークンからユーザーID取得
        user_id = 1
        item = item_usecase.create_item(req, user_id)
    except NotFoundError as err:
        logger.error(f"({__name__}): {err}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=err.message)
    except Exception as err:
        logger.error(f"({__name__}): {err}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    return item


@router.get("", response_model=list[ItemResponse])
def list_owned_items(
    pagination: PaginationQuery = Depends(),
    item_usecase: ItemUseCaseInterface = Depends(new_item_usecase),
) -> list[ItemResponse]:
    if pagination.after is not None and pagination.before is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only either `before` or `after` can be specified",
        )
    try:
        # TODO: headerのトークンからユーザーID取得
        user_id = 2
        return item_usecase.get_my_list(pagination, user_id)
    except Exception as err:
        logger.error(f"({__name__}): {err}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@router.get("/{item_id}")
def owned_item(item_id: int):
    return {
        "id": item_id,
        "name": "item name",
        "status": "available",
        "imageUrl": "http://example.com/test.png",
        "description": "description",
        "author": "author",
    }


@router.put("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def change_item():
    pass


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def del_item():
    pass
