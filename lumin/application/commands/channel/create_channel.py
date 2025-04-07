from lumin.domain.channel.channel import Channel
from lumin.infrastructure.repisitories.channel_repository import ChannelRepository


class CreateChannel:
    @staticmethod
    def create_channel(channel: Channel) -> None:
        ChannelRepository.add(channel)
