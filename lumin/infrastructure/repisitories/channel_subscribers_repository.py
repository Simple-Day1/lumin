from typing import Type
from uuid import UUID
from sqlalchemy import text
from lumin.domain.channel.channel import Channel
from lumin.domain.channel_subscriber.channel_subscriber import ChannelSubscriber
from lumin.domain.user.user import User
from lumin.infrastructure.database.config import PostgresConfig
from lumin.infrastructure.database.main import setup_engine, setup_connection
from lumin.infrastructure.repisitories.channel_repository import ChannelRepository
from lumin.infrastructure.repisitories.user_repository import UserRepository
from lumin.domain.channel_subscriber.exceptions import ChannelSubscriberIsNotExist, ChannelSubscriberIsAlreadyExist


class ChannelSubscriberRepository:
    @staticmethod
    def add(subscriber: ChannelSubscriber) -> None:
        try:
            command = text(
                """
                INSERT INTO subscribers_of_channels(subscribers_of_channel_id, channel_id, role)
                VALUES :subscribers_of_channel_id, :channel_id, :role
                """
            ).bindparams(
                subscribers_of_channel_id=subscriber.channel.channel_id,
                channel_id=subscriber.channel.channel_id,
                role=subscriber.role
            )
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                connection.execute(command)
        except Exception as e:
            raise ChannelSubscriberIsAlreadyExist(f"{e}")

    @staticmethod
    def delete(subscriber: ChannelSubscriber) -> None:
        try:
            command = text(
                """
                DELETE FROM subscribers_of_channels
                WHERE subscriber_id = :subscriber_id
                """
            ).bindparams(channel_id=subscriber.subscriber.user_id)
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                connection.execute(command)
        except Exception as e:
            raise ChannelSubscriberIsNotExist(f"{e}")

    @staticmethod
    def update(subscriber: ChannelSubscriber) -> None:
        try:
            command = text(
                """
                UPDATE subscribers_of_channels
                SET subscribers_of_channel_id = :subscribers_of_channel_id, channel_id = :channel_id, role = :role
                WHERE subscriber_id = :subscriber_id
                """
            ).bindparams(
                subscribers_of_channel_id=subscriber.subscriber.user_id,
                channel_id=subscriber.channel.channel_id,
                role=subscriber.role
            )
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                connection.execute(command)
        except Exception as e:
            raise ChannelSubscriberIsNotExist(f"{e}")

    @staticmethod
    async def with_id(subscriber_id: UUID) -> ChannelSubscriber | None:
        try:
            query = text(
                """
                SELECT subscribers_of_channel_id, channel_id, role
                FROM subscribers_of_channels
                WHERE subscriber_id = :subscriber_id
                """
            ).bindparams(subscriber_id=subscriber_id)
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                result = await connection.execute(query)
                row = result.fetchone()

            if not row:
                return None

            channel = ChannelRepository.with_id(row.channel_id)
            subscriber = UserRepository.with_id(row.subscribers_of_channel_id)

            if isinstance(channel, Channel) and isinstance(subscriber, User):
                return ChannelSubscriber(
                    channel=channel,
                    subscriber=subscriber,
                    role=row.role
                )
            else:
                return None
        except Exception as e:
            raise ChannelSubscriberIsNotExist(f"{e}")
