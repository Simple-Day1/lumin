from uuid import UUID
from lumin.infrastructure.repisitories.channel_repository import ChannelRepository


class DeleteSubscriberOfChannel:
    @staticmethod
    def delete_subscriber_of_channel(channel_id: UUID, subscriber_id: UUID) -> None:
        channel = ChannelRepository.with_id(channel_id)
        channel.admins.remove(subscriber_id)
        ChannelRepository.update(channel)
