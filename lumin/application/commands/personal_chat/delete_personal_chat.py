from lumin.domain.personal_сhat.personal_chat import PersonalChat
from lumin.infrastructure.repisitories.personal_chat_repository import PersonalChatRepository


class DeletePersonalChat:
    @staticmethod
    def delete_personal_chat(personal_chat: PersonalChat) -> None:
        PersonalChatRepository.delete(personal_chat)
