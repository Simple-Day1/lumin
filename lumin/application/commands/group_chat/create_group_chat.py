from lumin.domain.group_chat.group_chat import GroupChat
from lumin.infrastructure.repisitories.group_chat_repository import GroupChatRepository


class CreateGroupChat:
    @staticmethod
    def create_group_chat(group_chat: GroupChat) -> None:
        GroupChatRepository.add(group_chat)
