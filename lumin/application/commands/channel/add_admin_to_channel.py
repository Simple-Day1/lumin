from uuid import UUID
from lumin.infrastructure.repisitories.channel_repository import ChannelRepository


class AddAdminToChannel:
    @staticmethod
    def add_admin_to_channel(channel_id: UUID, admin_id: UUID) -> None:
        channel = ChannelRepository.with_id(channel_id)
        channel.admins.append(admin_id)
        ChannelRepository.update(channel)
