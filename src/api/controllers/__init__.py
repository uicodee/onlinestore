from fastapi import FastAPI
from .category import router as category_router


def setup(app: FastAPI) -> None:
    app.include_router(
        router=category_router,
        tags=["Category"]
    )
