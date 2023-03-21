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

    @classmethod
    def new(cls, id: int) -> "RentResponse":
        return cls(id=id)


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

    @classmethod
    def new(
        cls,
        id: int,
        closed: bool,
        rental_date: date,
        return_plan_date: date,
        return_date: Optional[date],
        item_id: int,
        item_name: str,
    ) -> "RentalResponse":
        return cls(
            id=id,
            closed=closed,
            rentalDate=rental_date,
            returnPlanDate=return_plan_date,
            returnDate=return_date,
            itemId=item_id,
            itemName=item_name,
        )
