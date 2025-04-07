from lumin.domain.user.user import User
from lumin.infrastructure.repisitories.user_repository import UserRepository


class DeleteUser:
    @staticmethod
    def delete_user(user: User) -> None:
        UserRepository.delete(user)
