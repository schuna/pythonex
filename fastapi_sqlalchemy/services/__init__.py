from typing import Iterator

from models.address import AddressDto
from models.user import User
from repositories import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._repository: UserRepository = user_repository

    def get_users(self) -> Iterator[User]:
        return self._repository.get_all()

    def get_user_by_id(self, user_id: int) -> User:
        return self._repository.get_by_id(user_id)

    def create_user(self, name: str, fullname: str, addresses: list[AddressDto]) -> User:
        return self._repository.add(name=name, fullname=fullname, addresses=addresses)

    def delete_user_by_id(self, user_id: int) -> None:
        return self._repository.delete_by_id(user_id)
