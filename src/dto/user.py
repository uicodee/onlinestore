from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):

    firstname: str = Field(alias="firstName")
    lastname: str = Field(alias="lastName")
    email: EmailStr
