from typing import Optional

import domain_model
from fastapi import Query
from pydantic import BaseModel, Field


class ItemListParams(BaseModel):
    available: Optional[str] = Field(Query(default=None))


class ItemResponse(BaseModel):
    id: int
    name: str
    status: domain_model.ItemStatus
    image_url: Optional[str] = Field(
        None, alias="imageUrl", example="http://example.com/test.png"
    )

    def __init__(
        self,
        id: int,
        name: str,
        status: domain_model.ItemStatus,
        image_url: Optional[str] = None,
    ):
        self.id = id
        self.name = name
        self.status = status
        self.image_url = image_url


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

    def __init__(self, id: int):
        self.id = id
