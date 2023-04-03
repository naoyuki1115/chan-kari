from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from auth.auth import get_authenticated_user
from database.database import get_db
from database.transaction import Transaction, TransactionInterface
from domain import Item, User
from repository import ItemStoreInterface, RentalStoreInterface
from schema import ItemCreateRequest, ItemCreateResponse, ItemResponse, PaginationQuery
from store import ItemStore, RentalStore
from usecase import ItemUseCase, ItemUseCaseInterface
from util.error_msg import NotFoundError, PaginationError
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
    user: User = Depends(get_authenticated_user),
) -> ItemCreateResponse:
    try:
        item: Item = item_usecase.create_item(req, user.get_user_id())
        return ItemCreateResponse.new(item.get_id())
    except NotFoundError as err:
        logger.error(f"({__name__}): {err}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=err.message)
    except Exception as err:
        logger.error(f"({__name__}): {err}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@router.get("", response_model=list[ItemResponse])
def list_owned_items(
    pagination: PaginationQuery = Depends(),
    item_usecase: ItemUseCaseInterface = Depends(new_item_usecase),
    user: User = Depends(get_authenticated_user),
) -> list[ItemResponse]:
    try:
        pagination.validate()

        items: list[Item] = item_usecase.get_my_list(pagination, user.get_user_id())
        item_res_list: list[ItemResponse] = []
        for item in items:
            item_res_list.append(
                ItemResponse.new(
                    item.get_id(),
                    item.get_name(),
                    item.get_status(),
                    item.get_image_url(),
                )
            )
        return item_res_list
    except PaginationError as err:
        logger.error(f"({__name__}): {err}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=err.message)
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
