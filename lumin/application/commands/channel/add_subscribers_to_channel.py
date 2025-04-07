from uuid import UUID
from lumin.infrastructure.repisitories.channel_repository import ChannelRepository


class AddSubscriberToChannel:
    @staticmethod
    def add_subscriber_to_channel(channel_id: UUID, subscriber_id: UUID) -> None:
        channel = ChannelRepository.with_id(channel_id)
        channel.subscribers.append(subscriber_id)
        ChannelRepository.update(channel)
