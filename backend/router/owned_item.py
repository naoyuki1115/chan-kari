from database.database import get_db
from database.transaction import Transaction, TransactionInterface
from fastapi import APIRouter, Depends, HTTPException, status
from schema import ItemCreateRequest, ItemCreateResponse
from sqlalchemy.orm import Session
from store import ItemStore, ItemStoreInterface, RentalStore, RentalStoreInterface
from usecase import ItemUseCase, ItemUseCaseInterface
from util.logging import get_logger

router = APIRouter(
    prefix="/items",
)


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
        test_user_id = 1
        item = item_usecase.create_item(req, test_user_id)
    except Exception as e:
        get_logger(__name__).error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    return item


@router.get("")
def list_owned():
    return [
        {
            "id": 1,
            "name": "item name",
            "status": "available",
            "imageUrl": "http://example.com/test.png",
        }
    ]


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
