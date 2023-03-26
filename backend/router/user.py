from fastapi import APIRouter, Depends, HTTPException, status
from firebase_admin.auth import UserRecord
from sqlalchemy.orm import Session

from auth.auth import authenticate_user
from database.database import get_db
from database.transaction import Transaction, TransactionInterface
from repository import UserStoreInterface
from schema import UserRegisterRequest
from store import UserStore
from usecase import UserUseCase, UserUseCaseInterface
from util.error_msg import InvalidTokenError, ResourceAlreadyExistsError
from util.logging import get_logger

logger = get_logger()
router = APIRouter()


def new_user_usecase(db: Session = Depends(get_db)) -> UserUseCaseInterface:
    tx: TransactionInterface = Transaction(db)
    user_store: UserStoreInterface = UserStore(db)
    return UserUseCase(tx, user_store)


@router.post("/signup", status_code=status.HTTP_204_NO_CONTENT)
def register_user(
    req: UserRegisterRequest,
    user_usecase: UserUseCaseInterface = Depends(new_user_usecase),
    idp_user: UserRecord = Depends(authenticate_user),
) -> None:
    try:
        if idp_user.uid is None or idp_user.email is None:
            raise InvalidTokenError
        user_usecase.create_user(
            uid=idp_user.uid,
            name=req.name,
            email=idp_user.email,
            image_url=idp_user.photo_url,
        )
    except InvalidTokenError as err:
        logger.error(f"({__name__}): {err}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=err.message
        )
    except ResourceAlreadyExistsError as err:
        logger.error(f"({__name__}): {err}")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User is already existed",
        )
    except Exception as err:
        logger.error(f"({__name__}): {err}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@router.get("/profile")
def profile():
    # Mock
    return {
        "name": "user name",
        "nickName": "nick name",
        "email": "example@mail.com",
        "imageUrl": "http://example.com/test.png",
    }


@router.put("/profile", status_code=status.HTTP_204_NO_CONTENT)
def change_nickname():
    pass
