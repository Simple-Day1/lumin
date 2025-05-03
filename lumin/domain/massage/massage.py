from datetime import datetime
from uuid import UUID
from lumin.domain.massage.value_objects import Reaction


class Massage:
    def __init__(
        self,
        massage_id: UUID,
        content: str,
        sender_id: UUID,
        recipient_id: UUID,
        timestamp: datetime,
        chat_id: UUID,
        photo_urls: list[str] | None,
        video_urls: list[str] | None,
        status: str,
        reaction_id: UUID | None,
        fixed: bool
    ) -> None:
        self.massage_id = massage_id
        self.content = content
        self.sender_id = sender_id
        self.recipient_id = recipient_id
        self.timestamp = timestamp
        self.chat_id = chat_id
        self.photo_urls = photo_urls
        self.video_urls = video_urls
        self.status = status
        self.reaction_id = reaction_id
        self.fixed = fixed
