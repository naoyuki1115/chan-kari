from typing import Optional

from fastapi import Query
from pydantic import BaseModel, Field


class PaginationQuery(BaseModel):
    limit: int = Field(Query(default=10))
    after: Optional[int] = Field(Query(default=None))
    before: Optional[int] = Field(Query(default=None))
