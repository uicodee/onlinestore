from fastapi import APIRouter, Path, Query
from src import dto
from src.api import schems

router = APIRouter(prefix="/user")


@router.get(
    path="/all",
    description="Get all users",
    response_model=list[dto.User]
)
async def get_users() -> list[dto.User]:
    ...


@router.get(
    path="/{user_id}",
    description="Get user by id",
    response_model=dto.User
)
async def get_user(
        user_id: int = Path()
) -> dto.User:
    ...


@router.post(
    path="/new",
    description="Create new user",
    response_model=dto.User
)
async def new_user(
        user: schems.User
) -> dto.User:
    ...


@router.put(
    path="/edit",
    description="Edit existing user",
    response_model=dto.User
)
async def edit_user(
        user: schems.EditUser
) -> dto.User:
    ...


@router.delete(
    path="/delete",
    description="Delete user"
)
async def delete_user(
        user_id: int = Query(alias="userId")
):
    ...

