from uuid import UUID
from massanger.domain.user.user import User
from massanger.infrastructure.repisitories.user_repository import UserRepository


class GetUserById:
    @staticmethod
    async def get_user_by_id(user_id: UUID) -> User | None:
        user = UserRepository.with_id(user_id)
        return user
