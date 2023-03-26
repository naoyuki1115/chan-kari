from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from firebase_admin import auth
from firebase_admin.auth import ExpiredIdTokenError, InvalidIdTokenError
from sqlalchemy.orm import Session

from database.database import get_db
from domain import User
from firebase_config.firebase import firebase_app
from repository import UserStoreInterface
from store import UserStore
from util.error_msg import UnauthorizedUserError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def new_user_store(db: Session = Depends(get_db)) -> UserStoreInterface:
    return UserStore(db)


def authenticate_user(
    token: str = Depends(oauth2_scheme),
    user_store: UserStoreInterface = Depends(new_user_store),
) -> User:
    try:
        decoded_token = auth.verify_id_token(token, app=firebase_app)
        uid = decoded_token["uid"]
        user = user_store.detailByUid(uid)
        if user is None:
            raise UnauthorizedUserError
        return user
    except ExpiredIdTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired"
        )
    except InvalidIdTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )
    except UnauthorizedUserError as err:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=err.message
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
