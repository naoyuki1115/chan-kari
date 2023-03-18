from typing import Any, Type, TypeVar

from schema import PaginationQuery
from sqlalchemy import desc
from sqlalchemy.orm import Query

T = TypeVar("T", bound=tuple)


def pagination_query(
    t: Type[T],
    q: Query,
    pagination: PaginationQuery,
    id: Any,
) -> list[T]:
    if pagination.after is not None:
        return (
            q.order_by(desc(id))
            .filter(id < pagination.after)
            .limit(pagination.limit)
            .all()
        )
    elif pagination.before is not None:
        resources = (
            q.order_by(id).offset(pagination.before).limit(pagination.limit).all()
        )
        resources.reverse()
        return resources
    else:
        return q.order_by(desc(id)).limit(pagination.limit).all()
