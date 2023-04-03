from typing import Optional

from psycopg2.errors import ForeignKeyViolation, UniqueViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from domain import User
from model import UserDTO
from repository import UserStoreInterface
from util.error_msg import NotFoundError, ResourceAlreadyExistsError
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

    def create(self, domain_user: User) -> None:
        try:
            user: UserDTO = UserDTO.from_domain_model(domain_user)
            self.db.add(user)
            # Note: 一時的にDBへ反映し、IDを取得
            self.db.flush()
            domain_user.set_id(user.id)
        except IntegrityError as err:
            logger.error(f"({__name__}): {err}")
            if isinstance(err.orig, UniqueViolation):
                raise ResourceAlreadyExistsError
            elif isinstance(err.orig, ForeignKeyViolation):
                raise NotFoundError
            else:
                raise err
        except Exception as err:
            logger.error(f"({__name__}): {err}")
            raise
