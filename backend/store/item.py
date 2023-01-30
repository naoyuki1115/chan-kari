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
        .order_by(desc(model.Item.id))
        .limit(limit)
    )
    if after is not None:
        return q.offset(after).all()
    elif before is not None:
        return q.offset(before).all()
    return q.all()
