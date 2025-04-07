from massanger.domain.user.user import User
from massanger.infrastructure.repisitories.user_repository import UserRepository


class CreateUser:
    @staticmethod
    def create_user(user: User) -> None:
        UserRepository.add(user)
