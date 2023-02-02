import model
from sqlalchemy.orm import Session


def list_not_returned(db: Session) -> list[model.Rental]:
    return (
        db.query(model.Rental)
        .filter(model.Rental.returned_at == None)  # NOQA
        .order_by(model.Rental.id)
        .all()
    )
