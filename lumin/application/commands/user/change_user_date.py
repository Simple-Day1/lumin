from uuid import UUID
from lumin.domain.user.value_objects import Date
from lumin.infrastructure.repisitories.user_repository import UserRepository


class ChangeUserDate:
    @staticmethod
    def change_user_date(user_id: UUID, new_date: Date) -> None:
        user = UserRepository.with_id(user_id)
        user.date = new_date
        UserRepository.update(user)
