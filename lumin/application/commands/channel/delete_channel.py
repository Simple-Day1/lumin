from lumin.domain.channel.channel import Channel
from lumin.infrastructure.repisitories.channel_repository import ChannelRepository


class DeleteChannel:
    @staticmethod
    def delete_channel(channel: Channel) -> None:
        ChannelRepository.delete(channel)
