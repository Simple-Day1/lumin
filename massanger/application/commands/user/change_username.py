from uuid import UUID
from massanger.infrastructure.repisitories.user_repository import UserRepository


class ChangeUsername:
    @staticmethod
    def change_user_phone(user_id: UUID, new_username: str) -> None:
        user = UserRepository.with_id(user_id)
        user.username = new_username
        UserRepository.update(user)
