from massanger.domain.user.user import User
from massanger.infrastructure.repisitories.user_repository import UserRepository


class DeleteUser:
    @staticmethod
    def delete_user(user: User) -> None:
        UserRepository.delete(user)
