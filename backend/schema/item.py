from enum import Enum
from typing import Optional

from fastapi import Query
from pydantic import BaseModel, Field
from schema.pagination import PaginationQuery


class Status(str, Enum):
    available = "available"
    unavailable = "unavailable"
    rented = "rented"


class ItemListQuery(BaseModel):
    status: Optional[Status] = Field(Query(default=None))


class ItemListRequest(ItemListQuery, PaginationQuery):
    pass


class ItemResponse(BaseModel):
    id: int
    name: str
    status: Status
    imageUrl: Optional[str] = Field(None, example="http://example.com/test.png")
