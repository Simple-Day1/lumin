from massanger.domain.channel.channel import Channel
from massanger.infrastructure.repisitories.channel_repository import ChannelRepository


class DeleteChannel:
    @staticmethod
    def delete_channel(channel: Channel) -> None:
        ChannelRepository.delete(channel)
