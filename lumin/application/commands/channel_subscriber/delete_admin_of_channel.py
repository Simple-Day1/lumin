from uuid import UUID
from lumin.infrastructure.repisitories.channel_repository import ChannelRepository


class DeleteAdminOfChannel:
    @staticmethod
    def delete_admin_of_channel(channel_id: UUID, admin_id: UUID):
        channel = ChannelRepository.with_id(channel_id)
        channel.admins.remove(admin_id)
        ChannelRepository.update(channel)
