import model
from sqlalchemy.orm import Session


def list_available(db: Session) -> list[model.Item]:
    return []
