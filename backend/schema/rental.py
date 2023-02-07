from datetime import date

from pydantic import BaseModel


class RentRequest(BaseModel):
    itemId: int
    rentalDate: date
    returnPlanDate: date


class RentResponse(BaseModel):
    id: int
