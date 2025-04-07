from uuid import UUID
from lumin.domain.user.value_objects import Phone
from lumin.infrastructure.repisitories.user_repository import UserRepository


class ChangeUserPhone:
    @staticmethod
    def change_user_phone(user_id: UUID, new_phone: Phone) -> None:
        user = UserRepository.with_id(user_id)
        user.phone = new_phone
        UserRepository.update(user)
