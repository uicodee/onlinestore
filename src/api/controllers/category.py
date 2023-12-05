from fastapi import APIRouter, Depends

from src.api import schems
from src.api.dependencies import dao_provider
from src.infrastructure.database.dao.holder import HolderDao


router = APIRouter(prefix="/category")


@router.get(path="/all")
async def get_categories(
        dao: HolderDao = Depends(dao_provider)
):
    ...


@router.get(path="/{category_id}")
async def get_category():
    ...


@router.post(path="/new")
async def new_category(
        category: schems.Category,
        dao: HolderDao = Depends(dao_provider)
):
    category = await dao.category.add_category(name=category.name)
    return {
        "id": category.id,
        "name": category.name
    }


@router.put(path="/edit")
async def edit_category():
    ...


@router.delete(path="/delete")
async def delete_category():
    ...


