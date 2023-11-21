from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):

    firstname: str = Field(alias="firstName")
    lastname: str = Field(alias="lastName")
    email: EmailStr
    password: str


class EditUser(BaseModel):

    firstname: str = Field(alias="firstName")
    lastname: str = Field(alias="lastName")
    user_id: int = Field(alias="userId")
