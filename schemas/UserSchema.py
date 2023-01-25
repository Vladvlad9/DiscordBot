from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    name_server: str
    name_user: str
    count: int


class UserInDBSchema(UserSchema):
    id: int = Field(ge=1)
