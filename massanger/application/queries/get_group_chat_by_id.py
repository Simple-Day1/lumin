from uuid import UUID
from massanger.domain.group_chat.group_chat import GroupChat
from massanger.infrastructure.repisitories.group_chat_repository import GroupChatRepository


class GetGroupChatById:
    @staticmethod
    async def get_group_chat_by_id(group_chat_id: UUID) -> GroupChat | None:
        group_chat = GroupChatRepository.with_id(group_chat_id)
        return group_chat
