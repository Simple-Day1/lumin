from uuid import UUID
from lumin.domain.user.value_objects import Phone, Date


class User:
    def __init__(
        self,
        user_id: UUID,
        username: str,
        description: str,
        phone: Phone,
        date: Date
    ) -> None:
        self.user_id = user_id
        self.username = username
        self.description = description
        self.phone = phone
        self.date = date
