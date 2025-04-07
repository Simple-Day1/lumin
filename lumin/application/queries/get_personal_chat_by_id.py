from uuid import UUID
from lumin.domain.personal_сhat.personal_chat import PersonalChat
from lumin.infrastructure.repisitories.massage_repository import MassageRepository


class GetPersonalChatById:
    @staticmethod
    async def get_personal_chat_by_id(personal_chat_id: UUID) -> PersonalChat | None:
        personal_chat = MassageRepository.with_id(personal_chat_id)
        return personal_chat
