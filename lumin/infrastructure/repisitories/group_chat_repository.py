from uuid import UUID

from lumin.domain.group_chat.exceptions import GroupChatIsAlreadyError, GroupChatIsNotExistError
from lumin.domain.group_chat.group_chat import GroupChat
from lumin.infrastructure.database.database import group_chats_database


class GroupChatRepository:
    @staticmethod
    def add(group_chat: GroupChat) -> None:
        if group_chat.group_chat_id in group_chats_database.keys():
            raise GroupChatIsAlreadyError('Group chat is already exist!')
        else:
            group_chats_database[group_chat.group_chat_id] = {
                'members': group_chat.members,
                'admins': group_chat.admins
            }

    @staticmethod
    def delete(group_chat: GroupChat) -> None:
        if group_chat.group_chat_id in group_chats_database.keys():
            group_chats_database.pop(group_chat.group_chat_id)
        else:
            raise GroupChatIsNotExistError('Group chat is not exist!')

    @staticmethod
    def update(group_chat: GroupChat) -> None:
        if group_chat.group_chat_id in group_chats_database.keys():
            group_chats_database[group_chat.group_chat_id] = {
                'members': group_chat.members,
                'admins': group_chat.admins
            }
        else:
            raise GroupChatIsNotExistError('Group chat is not exist!')

    @staticmethod
    def with_id(group_chat_id: UUID) -> GroupChat | None:
        if group_chat_id in group_chats_database.keys():
            return GroupChat(
                group_chat_id=group_chat_id,
                members=group_chats_database[group_chat_id]['members'],
                admins=group_chats_database[group_chat_id]['admins']
            )
        else:
            raise GroupChatIsNotExistError('Group chat is not exist!')
