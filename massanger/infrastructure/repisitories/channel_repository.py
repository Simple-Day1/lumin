from uuid import UUID

from massanger.domain.channel.channel import Channel
from massanger.domain.channel.exceptions import ChannelIsAlreadyExistError, ChannelIsNotExistError
from massanger.infrastructure.database.database import channels_database


class ChannelRepository:
    @staticmethod
    def add(channel: Channel) -> None:
        if channel.channel_id in channels_database.keys():
            raise ChannelIsAlreadyExistError('Channel is already exist!')
        else:
            channels_database[channel.channel_id] = {
                'channel_name': channel.channel_name,
                'channel_description': channel.channel_description,
                'subscribers': channel.subscribers,
                'admins': channel.admins,
                'public': channel.public
            }

    @staticmethod
    def delete(channel: Channel) -> None:
        if channel.channel_id in channels_database.keys():
            channels_database.pop(channel.channel_id)
        else:
            raise ChannelIsNotExistError('Channel is not exist!')

    @staticmethod
    def update(channel: Channel) -> None:
        if channel.channel_id in channels_database.keys():
            channels_database[channel.channel_id] = {
                'channel_name': channel.channel_name,
                'channel_description': channel.channel_description,
                'subscribers': channel.subscribers,
                'admins': channel.admins,
                'public': channel.public
            }
        else:
            raise ChannelIsNotExistError('Channel is not exist!')

    @staticmethod
    def with_id(channel_id: UUID) -> Channel | None:
        if channel_id in channels_database.keys():
            return Channel(
                channel_id=channel_id,
                channel_name=channels_database[channel_id]['channel_name'],
                channel_description=channels_database[channel_id]['channel_description'],
                subscribers=channels_database[channel_id]['subscribers'],
                admins=channels_database[channel_id]['admins'],
                public=channels_database[channel_id]['public']
            )
        else:
            raise ChannelIsNotExistError('Channel is not exist!')
