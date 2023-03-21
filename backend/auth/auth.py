from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from firebase_config.firebase import firebase_app
from firebase_admin import auth
from firebase_admin.auth import ExpiredIdTokenError, InvalidIdTokenError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def authenticate_user(token: str = Depends(oauth2_scheme)):
    try:
        decoded_token = auth.verify_id_token(token, app=firebase_app)
        uid = decoded_token["uid"]
        return uid
    except ExpiredIdTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired"
        )
    except InvalidIdTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
