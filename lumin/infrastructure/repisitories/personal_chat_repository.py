from uuid import UUID
from lumin.domain.personal_сhat.exceptions import PersonalChatIsAlreadyExistError, PersonalChatIsNotExistError
from lumin.domain.personal_сhat.personal_chat import PersonalChat


class PersonalChatRepository:
    @staticmethod
    def add(personal_chat: PersonalChat) -> None:
        ...

    @staticmethod
    def update(personal_chat: PersonalChat) -> None:
        ...

    @staticmethod
    def delete(personal_chat: PersonalChat) -> None:
        ...

    @staticmethod
    def with_id(personal_chat_id: UUID) -> PersonalChat | None:
        ...
