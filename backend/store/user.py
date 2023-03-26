from typing import Optional
from model import UserDTO
from domain import User
from repository import UserStoreInterface
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from util.logging import get_logger

logger = get_logger()


class UserStore(UserStoreInterface):
    def __init__(self, session: Session) -> None:
        self.db = session

    def detailByUid(self, uid: str) -> Optional[User]:
        try:
            user: UserDTO = self.db.query(UserDTO).filter(UserDTO.uid == uid).one()
            return user.to_domain_model()
        except NoResultFound as err:
            logger.info(f"({__name__}): {err}")
            return None
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise
