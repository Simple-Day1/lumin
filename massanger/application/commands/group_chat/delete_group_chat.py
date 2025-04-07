from massanger.domain.group_chat.group_chat import GroupChat
from massanger.infrastructure.repisitories.group_chat_repository import GroupChatRepository


class DeleteGroupChat:
    @staticmethod
    def delete_group_chat(group_chat: GroupChat) -> None:
        GroupChatRepository.delete(group_chat)
