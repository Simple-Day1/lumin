from uuid import UUID


class GroupChat:
    def __init__(self, group_chat_id: UUID, members: list[UUID], admins: list[UUID]) -> None:
        self.group_chat_id = group_chat_id
        self.members = members
        self.admins = admins
