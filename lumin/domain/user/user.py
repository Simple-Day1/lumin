from uuid import UUID
from lumin.domain.user.value_objects import Phone, Date


class User:
    def __init__(
        self,
        user_id: UUID,
        username: str,
        email: str,
        description: str,
        phone: Phone,
        date: Date,
        user_avatar_url: str,
    ) -> None:
        self.user_id = user_id
        self.username = username
        self.email = email
        self.description = description
        self.phone = phone
        self.date = date
        self.user_avatar_url = user_avatar_url
