from datetime import date

from pydantic import BaseModel, Field


class RentRequest(BaseModel):
    item_id: int = Field(alias="itemId")
    rental_date: date = Field(alias="rentalDate")
    return_plan_date: date = Field(alias="returnPlanDate")


class RentResponse(BaseModel):
    id: int

    @classmethod
    def new(cls, id):
        return cls(id=id)
