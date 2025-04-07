from uuid import UUID
from massanger.infrastructure.repisitories.channel_repository import ChannelRepository


class ChangeChannelDescription:
    @staticmethod
    def change_channel_description(channel_id: UUID, new_description: str) -> None:
        channel = ChannelRepository.with_id(channel_id)
        channel.channel_description = new_description
        ChannelRepository.update(channel)
