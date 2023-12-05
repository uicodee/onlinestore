from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.infrastructure.database.dao.rdb import BaseDAO
from src.infrastructure.database.models import Category


class CategoryDAO(BaseDAO[Category]):
    def __init__(self, session: AsyncSession):
        super().__init__(Category, session)

    async def get_categories(self):
        result = await self.session.execute(
            select(Category)
        )
        return result.scalars().all()

    async def get_category(self, category_id: int):
        result = await self.session.execute(
            select(Category).where(Category.id == category_id)
        )
        return result.scalar()

    async def add_category(self, name: str) -> dto.Category:
        result = await self.session.execute(
            insert(Category).values(
                name=name
            ).returning(Category)
        )
        await self.session.commit()
        return result.scalar()
        # return dto.Category.model_dump_json(result.scalar())