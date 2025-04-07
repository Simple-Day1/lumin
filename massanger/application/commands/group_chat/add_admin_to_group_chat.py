from uuid import UUID
from massanger.infrastructure.repisitories.group_chat_repository import GroupChatRepository


class AddAdminToGroupChat:
    @staticmethod
    def add_admin_to_group_chat(group_chat_id: UUID, admin_id: UUID) -> None:
        group_chat = GroupChatRepository.with_id(group_chat_id)
        group_chat.admins.append(admin_id)
        GroupChatRepository.update(group_chat)
