from typing import Optional

import model
from sqlalchemy.orm import Session


def list_available(
    db: Session, limit: int, after: Optional[int], before: Optional[int]
) -> list[model.Item]:
    return []
