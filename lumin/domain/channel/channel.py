from uuid import UUID


class Channel:
    def __init__(
        self,
        channel_id: UUID,
        channel_name: str,
        channel_description: str,
        subscribers: list[UUID],
        admins: list[UUID],
        public: bool
    ) -> None:
        self.channel_id = channel_id
        self.channel_name = channel_name
        self.channel_description = channel_description
        self.subscribers = subscribers
        self.admins = admins
        self.public = public
