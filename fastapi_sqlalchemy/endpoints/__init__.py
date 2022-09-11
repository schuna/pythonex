from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Response, status

from containers import Container
from models.user import UserDto
from repositories import NotFoundError
from services import UserService

router = APIRouter()


@router.get("/users")
@inject
def get_list(
        user_service: UserService = Depends(Provide[Container.user_service]),
):
    return user_service.get_users()


@router.get("/users/{user_id}")
@inject
def get_by_id(
        user_id: int,
        user_service: UserService = Depends(Provide[Container.user_service]),
):
    try:
        return user_service.get_user_by_id(user_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/users", status_code=status.HTTP_201_CREATED)
@inject
def add(
        user: UserDto,
        user_service: UserService = Depends(Provide[Container.user_service]),
):
    return user_service.create_user(user.name, user.fullname, user.addresses)


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def remove(
        user_id: int,
        user_service: UserService = Depends(Provide[Container.user_service]),
):
    try:
        user_service.delete_user_by_id(user_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    finally:
        return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/status")
def get_status():
    return {"status": "Ok"}
