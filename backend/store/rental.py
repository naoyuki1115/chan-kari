import model
from sqlalchemy.orm import Session


def list_rented(db: Session) -> list[model.Rental]:
    return []
