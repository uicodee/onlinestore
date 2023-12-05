from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.database.models import BaseModel


class Category(BaseModel):

    __tablename__ = "category"

    name: Mapped[str] = mapped_column(String)
