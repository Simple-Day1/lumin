from massanger.domain.channel.channel import Channel
from massanger.infrastructure.repisitories.channel_repository import ChannelRepository


class CreateChannel:
    @staticmethod
    def create_channel(channel: Channel) -> None:
        ChannelRepository.add(channel)
