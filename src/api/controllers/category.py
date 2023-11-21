from fastapi import APIRouter

router = APIRouter(prefix="/category")


@router.get(path="/all")
async def get_categories():
    ...


@router.get(path="/{category_id}")
async def get_category():
    ...


@router.post(path="/new")
async def new_category():
    ...


@router.put(path="/edit")
async def edit_category():
    ...


@router.delete(path="/delete")
async def delete_category():
    ...


