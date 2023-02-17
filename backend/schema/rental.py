from datetime import date
from typing import Optional

from fastapi import Path, Query
from pydantic import BaseModel, Field
from schema.pagination import PaginationQuery


class RentRequest(BaseModel):
    item_id: int = Field(alias="itemId")
    rental_date: date = Field(alias="rentalDate")
    return_plan_date: date = Field(alias="returnPlanDate")


class RentResponse(BaseModel):
    id: int

    @classmethod
    def new(cls, id):
        return cls(id=id)


class ReturnParams(BaseModel):
    rental_id: int = Field(Path(alias="rentalId"))


class RentalListParams(PaginationQuery):
    closed: Optional[str] = Field(Query(default=None))


class RentalResponse(BaseModel):
    id: int
    closed: bool
    rental_date: date = Field(alias="rentalDate")
    return_plan_date: date = Field(alias="returnPlanDate")
    return_date: Optional[date] = Field(alias="returnDate")
    item_id: int = Field(alias="itemId")
    item_name: str = Field(alias="itemName")

    @classmethod
    def new(
        cls, id, closed, rental_date, return_plan_date, return_date, item_id, item_name
    ):
        return cls(
            id=id,
            closed=closed,
            rentalDate=rental_date,
            returnPlanDate=return_plan_date,
            returnDate=return_date,
            itemId=item_id,
            itemName=item_name,
        )
