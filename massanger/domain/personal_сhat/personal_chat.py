from uuid import UUID


class PersonalChat:
    def __init__(self, personal_chat_id: UUID) -> None:
        self.personal_chat_id = personal_chat_id
