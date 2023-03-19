from datetime import date
from typing import Optional

from fastapi import Path, Query
from pydantic import BaseModel, Field


class RentRequest(BaseModel):
    item_id: int = Field(alias="itemId")
    rental_date: date = Field(alias="rentalDate")
    return_plan_date: date = Field(alias="returnPlanDate")


class RentResponse(BaseModel):
    id: int

    def __init__(self, id: int):
        self.id = id


class ReturnParams(BaseModel):
    rental_id: int = Field(Path(alias="rentalId"))


class RentalListParams(BaseModel):
    closed: Optional[str] = Field(Query(default=None))


class RentalResponse(BaseModel):
    id: int
    closed: bool
    rental_date: date = Field(alias="rentalDate")
    return_plan_date: date = Field(alias="returnPlanDate")
    return_date: Optional[date] = Field(alias="returnDate")
    item_id: int = Field(alias="itemId")
    item_name: str = Field(alias="itemName")

    def __init__(
        self,
        id: int,
        closed: bool,
        rental_date: date,
        return_plan_date: date,
        return_date: Optional[date],
        item_id: int,
        item_name: str,
    ):
        self.id = id
        self.closed = closed
        self.rental_date = rental_date
        self.return_plan_date = return_plan_date
        self.return_date = return_date
        self.item_id = item_id
        self.item_name = item_name
