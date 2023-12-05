from pydantic import BaseModel, ConfigDict


class Category(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str


