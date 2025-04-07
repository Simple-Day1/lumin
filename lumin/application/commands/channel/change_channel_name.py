from uuid import UUID
from lumin.infrastructure.repisitories.channel_repository import ChannelRepository


class ChangeChannelName:
    @staticmethod
    def change_channel_description(channel_id: UUID, new_name: str) -> None:
        channel = ChannelRepository.with_id(channel_id)
        channel.channel_name = new_name
        ChannelRepository.update(channel)
