from datetime import date

from pydantic import BaseModel


class RentRequest(BaseModel):
    itemId: int
    rentalDate: date
    returnPlanDate: date


class RentResponse(BaseModel):
    id: int

    @classmethod
    def new(cls, id):
        return cls(id=id)
