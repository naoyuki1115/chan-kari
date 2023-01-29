import model
from sqlalchemy import desc
from sqlalchemy.orm import Session


def list_not_returned(db: Session) -> list[model.Rental]:
    return (
        db.query(model.Rental)
        .filter(model.Rental.returned_at is not None)
        .order_by(desc(model.Rental.id))
        .all()
    )
