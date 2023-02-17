from database.database import get_db
from database.transaction import Transaction, TransactionInterface
from fastapi import APIRouter, Depends, HTTPException, status
from schema import (
    RentalListParams,
    RentalResponse,
    RentRequest,
    RentResponse,
    ReturnParams,
)
from sqlalchemy.orm import Session
from store import ItemStore, ItemStoreInterface, RentalStore, RentalStoreInterface
from usecase import RentalUseCase, RentalUseCaseInterface
from util.error_msg import (
    NotFoundError,
    OperationIsForbiddenError,
    ResourceAlreadyExistsError,
    ResourceUnavailableError,
)
from util.logging import get_logger

router = APIRouter()

logger = get_logger()


def new_rental_usecase(db: Session = Depends(get_db)) -> RentalUseCaseInterface:
    tx: TransactionInterface = Transaction(db)
    item_store: ItemStoreInterface = ItemStore(db)
    renal_store: RentalStoreInterface = RentalStore(db)
    return RentalUseCase(tx, item_store, renal_store)


@router.get("", response_model=list[RentalResponse])
def list_rental(
    params: RentalListParams = Depends(),
    rental_usecase: RentalUseCaseInterface = Depends(new_rental_usecase),
):
    try:
        # TODO: headerのトークンからユーザーID取得
        user_id = 2
        return rental_usecase.get_my_list(params, user_id)
    except Exception as err:
        logger.error(f"({__name__}): {err}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@router.get("/{item_id}")
def get_rental(item_id: int):
    return [
        {
            "itemId": item_id,
            "rentalDate": "2022-06-06",
            "returnPlanDate": "2022-06-06",
        }
    ]


@router.post("", response_model=RentResponse)
def rent_item(
    req: RentRequest,
    rental_usecase: RentalUseCaseInterface = Depends(new_rental_usecase),
) -> RentResponse:
    try:
        # TODO: headerのトークンからユーザーID取得
        user_id = 2
        return rental_usecase.rent_item(req, user_id)
    except NotFoundError as err:
        logger.error(f"({__name__}): {err}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item ID is not found"
        )
    except OperationIsForbiddenError as err:
        logger.error(f"({__name__}): {err}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Don't be allowed to rent this Item",
        )
    except ResourceUnavailableError as err:
        logger.error(f"({__name__}): {err}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=err.message)
    except ResourceAlreadyExistsError as err:
        logger.error(f"({__name__}): {err}")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Item is already rented by another user",
        )
    except Exception as err:
        logger.error(f"({__name__}): {err}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@router.put("/{rentalId}/return", status_code=status.HTTP_204_NO_CONTENT)
def return_rental(
    params: ReturnParams = Depends(),
    rental_usecase: RentalUseCaseInterface = Depends(new_rental_usecase),
):
    try:
        # TODO: headerのトークンからユーザーID取得
        user_id = 3
        rental_usecase.return_item(params, user_id)
    except NotFoundError as err:
        logger.error(f"({__name__}): {err}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Rental ID is not found"
        )
    except OperationIsForbiddenError as err:
        logger.error(f"({__name__}): {err}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This rental ID is not your rental",
        )
    except ResourceAlreadyExistsError as err:
        logger.error(f"({__name__}): {err}")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This Rental is already returned",
        )
    except Exception as err:
        logger.error(f"({__name__}): {err}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
