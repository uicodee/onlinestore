from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.database.dao.rdb import BaseDAO


class OrderDAO(BaseDAO[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)