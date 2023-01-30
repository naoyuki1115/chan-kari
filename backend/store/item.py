from typing import Optional

import model
from sqlalchemy import desc
from sqlalchemy.orm import Session


def list_available(
    db: Session, limit: int, after: Optional[int], before: Optional[int]
) -> list[model.Item]:
    q = (
        db.query(model.Item)
        .filter(model.Item.available == True)
        .order_by(model.Item.id)
    )
    if after is not None:
        q = q.offset(after)
    elif before is not None:
        q = q.filter(model.Item.id < before)
    return q.limit(limit).all()
