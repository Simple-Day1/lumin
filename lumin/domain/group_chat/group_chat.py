from uuid import UUID


class GroupChat:
    def __init__(
        self,
        group_chat_id: UUID,
        group_chat_name: str,
        group_chat_avatar_url: str
    ) -> None:
        self.group_chat_id = group_chat_id
        self.group_chat_name = group_chat_name
        self.group_chat_avatar_url = group_chat_avatar_url
