from uuid import UUID
from massanger.domain.channel.channel import Channel
from massanger.infrastructure.repisitories.channel_repository import ChannelRepository


class GetChannelById:
    @staticmethod
    async def get_channel_by_id(channel_id: UUID) -> Channel | None:
        channel = ChannelRepository.with_id(channel_id)
        return channel
