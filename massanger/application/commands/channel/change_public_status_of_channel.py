from uuid import UUID
from massanger.infrastructure.repisitories.channel_repository import ChannelRepository


class ChangeChannelPublicStatus:
    @staticmethod
    def change_channel_description(channel_id: UUID, new_public_status: str) -> None:
        channel = ChannelRepository.with_id(channel_id)
        channel.public = new_public_status
        ChannelRepository.update(channel)
