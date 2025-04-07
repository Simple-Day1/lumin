from lumin.domain.personal_сhat.personal_chat import PersonalChat
from lumin.infrastructure.repisitories.personal_chat_repository import PersonalChatRepository


class CreatePersonalChat:
    @staticmethod
    def create_personal_chat(personal_chat: PersonalChat) -> None:
        PersonalChatRepository.add(personal_chat)
