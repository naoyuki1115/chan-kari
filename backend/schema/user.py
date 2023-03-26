from pydantic import BaseModel, Field


class UserRegisterRequest(BaseModel):
    name: str = Field(alias="name")
