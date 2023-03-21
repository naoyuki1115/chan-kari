from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.database import get_db
from database.transaction import Transaction, TransactionInterface
from domain import Rental, RentalStatus
from repository import ItemStoreInterface, RentalStoreInterface
from schema import (
    PaginationQuery,
    RentalListParams,
    RentalResponse,
    RentRequest,
    RentResponse,
    ReturnParams,
)
from store import ItemStore, RentalStore
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
    pagination: PaginationQuery = Depends(),
    rental_usecase: RentalUseCaseInterface = Depends(new_rental_usecase),
) -> list[RentalResponse]:
    if pagination.after is not None and pagination.before is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only either `before` or `after` can be specified",
        )
    try:
        # TODO: headerのトークンからユーザーID取得
        user_id = 2
        rentals: list[Rental] = rental_usecase.get_my_list(pagination, params, user_id)
        rental_res_list: list[RentalResponse] = []
        for rental in rentals:
            if rental.get_status() == RentalStatus.returned:
                closed = True
            else:
                closed = False
            rental_res_list.append(
                RentalResponse.new(
                    rental.get_id(),
                    closed,
                    rental.get_rented_date(),
                    rental.get_return_plan_date(),
                    rental.get_returned_date(),
                    rental.get_item().get_id(),
                    rental.get_item().get_name(),
                )
            )
        return rental_res_list
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
        rental: Rental = rental_usecase.rent_item(req, user_id)
        return RentResponse.new(rental.get_id())
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
) -> None:
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
