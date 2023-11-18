from fastapi import APIRouter

from src import dto

router = APIRouter(prefix="/user")


@router.get(
    path="/all",
    description="Get all users",
    response_model=list[dto.User]
)
async def get_users() -> list[dto.User]:
    ...


@router.post(
    path="/new",
    description="Create new user",
    response_model=dto.User
)
async def new_user() -> dto.User:
    ...


@router.put(
    path="/edit",
    description="Edit existing user",
    response_model=dto.User
)
async def edit_user() -> dto.User:
    ...


@router.delete(
    path="/delete",
    description="Delete user"
)
async def delete_user():
    ...

