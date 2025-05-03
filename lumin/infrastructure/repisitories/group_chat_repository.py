from typing import Type
from uuid import UUID
from sqlalchemy import text
from lumin.domain.group_chat.exceptions import GroupChatIsAlreadyError, GroupChatIsNotExistError
from lumin.domain.group_chat.group_chat import GroupChat
from lumin.infrastructure.database.config import PostgresConfig
from lumin.infrastructure.database.main import setup_engine, setup_connection


class GroupChatRepository:
    @staticmethod
    def add(group_chat: GroupChat) -> None:
        try:
            command = text(
                """
                INSERT INTO group_chats(group_chat_id, group_chat_name, group_chat_avatar_url)
                VALUES :group_chat_id, :group_chat_name, :group_chat_avatar_url)
                """
            ).bindparams(
                group_chat_id=group_chat.group_chat_id,
                group_chat_name=group_chat.group_chat_name,
                group_chat_avatar_url=group_chat.group_chat_avatar_url
            )
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                connection.execute(command)
        except Exception as e:
            raise GroupChatIsAlreadyError(f"{e}")

    @staticmethod
    def delete(group_chat: GroupChat) -> None:
        try:
            command = text(
                """
                DELETE FROM group_chats
                WHERE group_chat_id = :group_chat_id
                """
            ).bindparams(group_chat_id=group_chat.group_chat_id)
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                connection.execute(command)
        except Exception as e:
            raise GroupChatIsNotExistError(f"{e}")

    @staticmethod
    def update(group_chat: GroupChat) -> None:
        try:
            command = text(
                """
                UPDATE group_chats
                SET group_chat_id = :group_chat_id, group_chat_name = :group_chat_name, group_chat_avatar_url = :group_chat_avatar_url
                WHERE group_chat_id = :group_chat_id
                """
            ).bindparams(
                group_chat_id=group_chat.group_chat_id,
                group_chat_name=group_chat.group_chat_name,
                group_chat_avatar_url=group_chat.group_chat_avatar_url
            )
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                connection.execute(command)
        except Exception as e:
            raise GroupChatIsNotExistError(f"{e}")

    @staticmethod
    async def with_id(group_chat_id: UUID) -> GroupChat | None:
        try:
            query = text(
                """
                SELECT group_chat_id, group_chat_name, group_chat_avatar_url
                FROM group_chats
                WHERE group_chat_id = :group_chat_id
                """
            ).bindparams(group_chat_id=group_chat_id)
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                result = await connection.execute(query)
                row = result.fetchone()

            if not row:
                return None

            return GroupChat(
                group_chat_id=row.group_chat_id,
                group_chat_name=row.group_chat_name,
                group_chat_avatar_url=row.group_chat_avatar_url
            )
        except Exception as e:
            raise GroupChatIsNotExistError(f"{e}")
