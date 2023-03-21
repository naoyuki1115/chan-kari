from typing import Optional

from fastapi import Query
from pydantic import BaseModel, Field

from domain.item import ItemStatus


class ItemListParams(BaseModel):
    available: Optional[str] = Field(Query(default=None))

    def validate(self):
        if (
            self.available == "false"
            or self.available == "False"
            or self.available == "f"
            or self.available == "F"
        ):
            self.available = None


class ItemResponse(BaseModel):
    id: int
    name: str
    status: ItemStatus
    image_url: Optional[str] = Field(
        None, alias="imageUrl", example="http://example.com/test.png"
    )

    @classmethod
    def new(
        cls,
        id: int,
        name: str,
        status: ItemStatus,
        image_url: Optional[str] = None,
    ) -> "ItemResponse":
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
    def new(cls, id: int) -> "ItemCreateResponse":
        return cls(id=id)
