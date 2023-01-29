from enum import Enum
from typing import Optional

from fastapi import Query
from pydantic import BaseModel, Field
from schema.pagination import PaginationQuery


class ItemStatus(str, Enum):
    available = "available"
    unavailable = "unavailable"
    rented = "rented"


class ItemListQuery(BaseModel):
    available: Optional[str] = Field(Query(default=None))


class ItemListRequest(ItemListQuery, PaginationQuery):
    pass


class ItemResponse(BaseModel):
    id: int
    name: str
    status: ItemStatus
    imageUrl: Optional[str] = Field(None, example="http://example.com/test.png")

    def __init__(self, id, name, status, imageUrl) -> None:
        self.id = id
        self.name = name
        self.status = status
        self.imageUrl = imageUrl
