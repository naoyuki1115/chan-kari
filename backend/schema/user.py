from pydantic import BaseModel, Field


class UserRegisterRequest(BaseModel):
    nickname: str = Field(alias="nickname")
