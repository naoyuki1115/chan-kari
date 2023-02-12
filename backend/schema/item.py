from enum import Enum
from typing import Optional

from fastapi import Query
from pydantic import BaseModel, Field
from schema.pagination import PaginationQuery


class ItemStatus(str, Enum):
    available = "available"
    unavailable = "unavailable"
    rented = "rented"


class ItemListParams(PaginationQuery):
    available: Optional[str] = Field(Query(default=None))


class ItemResponse(BaseModel):
    id: int
    name: str
    status: ItemStatus
    image_url: Optional[str] = Field(
        None, alias="imageUrl", example="http://example.com/test.png"
    )

    @classmethod
    def new(cls, id, name, status, image_url):
        return cls(id=id, name=name, status=status, imageUrl=image_url)


class ItemCreateRequest(BaseModel):
    name: str
    draft: bool
    image_url: Optional[str] = Field(
        None, alias="imageUrl", example="http://example.com/test.png"
    )
    description: Optional[str] = Field(None)
    author: Optional[str] = Field(None)


class ItemCreateResponse(BaseModel):
    id: int

    @classmethod
    def new(cls, id):
        return cls(id=id)
