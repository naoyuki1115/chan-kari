from typing import Optional

import model
from sqlalchemy import desc
from sqlalchemy.orm import Session


def list_available(
    db: Session, limit: int, after: Optional[int], before: Optional[int]
) -> list[model.Item]:
    q = db.query(model.Item).filter(model.Item.available == True)
    if after is not None:
        return q.order_by(model.Item.id).offset(after).limit(limit).all()
    elif before is not None:
        items = (
            q.order_by(desc(model.Item.id))
            .filter(model.Item.id < before)
            .limit(limit)
            .all()
        )
        items.reverse()
        return items
    else:
        return q.order_by(model.Item.id).limit(limit).all()
