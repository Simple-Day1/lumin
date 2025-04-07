from uuid import UUID
from massanger.infrastructure.repisitories.group_chat_repository import GroupChatRepository


class DeleteMemberToGroupChat:
    @staticmethod
    def delete_admin_to_group_chat(group_chat_id: UUID, member_id: UUID) -> None:
        group_chat = GroupChatRepository.with_id(group_chat_id)
        group_chat.members.append(member_id)
        GroupChatRepository.update(group_chat)
