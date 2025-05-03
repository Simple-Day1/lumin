from typing import Type
from uuid import UUID
from sqlalchemy import text
from lumin.domain.channel.channel import Channel
from lumin.domain.channel.exceptions import ChannelIsAlreadyExistError, ChannelIsNotExistError
from lumin.infrastructure.database.config import PostgresConfig
from lumin.infrastructure.database.main import setup_engine, setup_connection


class ChannelRepository:
    @staticmethod
    def add(channel: Channel) -> None:
        try:
            command = text(
                """
                INSERT INTO channels(channel_id, channel_name, channel_description, channel_public_status, channel_avatar_url)
                VALUES :channel_id, :channel_name, :channel_description, :public, :channel_avatar_url)
                """
            ).bindparams(
                channel_id=channel.channel_id,
                channel_name=channel.channel_name,
                channel_description=channel.channel_description,
                public=channel.public,
                channel_avatar_url=channel.channel_avatar_url
            )
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                connection.execute(command)
        except Exception as e:
            raise ChannelIsAlreadyExistError(f"{e}")

    @staticmethod
    def delete(channel: Channel) -> None:
        try:
            command = text(
                """
                DELETE FROM channels
                WHERE channel_id = :channel_id
                """
            ).bindparams(channel_id=channel.channel_id)
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                connection.execute(command)
        except Exception as e:
            raise ChannelIsNotExistError(f"{e}")

    @staticmethod
    def update(channel: Channel) -> None:
        try:
            command = text(
                """
                UPDATE channels
                SET channel_id = :channel_id, channel_name = :channel_name, channel_description = :channel_description, channel_public_status = :public, channel_avatar_url = :channel_avatar_url
                WHERE channel_id = :channel_id
                """
            ).bindparams(
                channel_id=channel.channel_id,
                channel_name=channel.channel_name,
                channel_description=channel.channel_description,
                public=channel.public,
                channel_avatar_url=channel.channel_avatar_url
            )
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                connection.execute(command)
        except Exception as e:
            raise ChannelIsNotExistError(f"{e}")

    @staticmethod
    async def with_id(channel_id: UUID) -> Channel | None:
        try:
            query = text(
                """
                SELECT channel_id, channel_name, channel_description, channel_public_status, channel_avatar_url
                FROM channels
                WHERE channel_id = :channel_id
                """
            ).bindparams(channel_id=channel_id)
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                result = await connection.execute(query)
                row = result.fetchone()

            if not row:
                return None

            return Channel(
                channel_id=channel_id,
                channel_name=row.channel_name,
                channel_description=row.channel_description,
                public=row.channel_public_status,
                channel_avatar_url=row.channel_avatar_url
            )
        except Exception as e:
            raise ChannelIsNotExistError(f"{e}")
