from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from src.api.dependencies.database import DbProvider, dao_provider


def setup(
        app: FastAPI,
        pool: sessionmaker,
):
    db_provider = DbProvider(pool=pool)
    app.dependency_overrides[dao_provider] = db_provider.dao
