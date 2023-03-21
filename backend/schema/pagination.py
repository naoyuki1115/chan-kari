from typing import Optional

from fastapi import Query
from pydantic import BaseModel, Field

from util.error_msg import PaginationError


class PaginationQuery(BaseModel):
    limit: int = Field(Query(default=10))
    after: Optional[int] = Field(Query(default=None))
    before: Optional[int] = Field(Query(default=None))

    def validate(self):
        if self.after is not None and self.before is not None:
            raise PaginationError
