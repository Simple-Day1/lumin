from uuid import UUID
from lumin.infrastructure.repisitories.user_repository import UserRepository


class ChangeUserDescription:
    @staticmethod
    def change_user_date(user_id: UUID, new_description: str) -> None:
        user = UserRepository.with_id(user_id)
        user.description = new_description
        UserRepository.update(user)
