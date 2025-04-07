from uuid import UUID
from lumin.infrastructure.database.database import personal_chats_database
from lumin.domain.personal_сhat.exceptions import PersonalChatIsAlreadyExistError, PersonalChatIsNotExistError
from lumin.domain.personal_сhat.personal_chat import PersonalChat


class PersonalChatRepository:
    @staticmethod
    def add(personal_chat: PersonalChat) -> None:
        if personal_chat.personal_chat_id in personal_chats_database.keys():
            raise PersonalChatIsAlreadyExistError('Personal chat is already exist!')
        else:
            personal_chats_database[personal_chat.personal_chat_id] = {'members': personal_chat.members}

    @staticmethod
    def update(personal_chat: PersonalChat) -> None:
        if personal_chat.personal_chat_id in personal_chats_database.keys():
            personal_chats_database[personal_chat.personal_chat_id] = {'members': personal_chat.members}
        else:
            raise PersonalChatIsNotExistError('Personal chat is not exist!')

    @staticmethod
    def delete(personal_chat: PersonalChat) -> None:
        if personal_chat.personal_chat_id in personal_chats_database.keys():
            personal_chats_database.pop(personal_chat.personal_chat_id)
        else:
            raise PersonalChatIsNotExistError('Personal chat is not exist!')

    @staticmethod
    def with_id(personal_chat_id: UUID) -> PersonalChat | None:
        if personal_chat_id in personal_chats_database.keys():
            return PersonalChat(
                personal_chat_id=personal_chat_id,
                members=personal_chats_database[personal_chat_id]['members']
            )
        else:
            raise PersonalChatIsNotExistError('Personal chat is not exist!')
