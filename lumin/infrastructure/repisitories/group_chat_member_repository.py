from typing import Type
from uuid import UUID
from sqlalchemy import text
from lumin.domain.group_chat.group_chat import GroupChat
from lumin.domain.group_chat_member.group_chat_member import GroupChatMember
from lumin.domain.group_chat_member.exceptions import GroupChatMemberIsNotExist, GroupChatMemberIsAlreadyExist
from lumin.domain.user.user import User
from lumin.infrastructure.database.config import PostgresConfig
from lumin.infrastructure.database.main import setup_engine, setup_connection
from lumin.infrastructure.repisitories.group_chat_repository import GroupChatRepository
from lumin.infrastructure.repisitories.user_repository import UserRepository


class GroupChatMemberRepository:
    @staticmethod
    def add(member: GroupChatMember) -> None:
        try:
            command = text(
                """
                INSERT INTO group_chats_members(group_chat_member_id, group_chat_id, role)
                VALUES :group_chat_member_id, :group_chat_id, :role
                """
            ).bindparams(
                group_chat_member_id=member.member.user_id,
                group_chat_id=member.group_chat.group_chat_id,
                role=member.role
            )
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                connection.execute(command)
        except Exception as e:
            raise GroupChatMemberIsAlreadyExist(f"{e}")

    @staticmethod
    def delete(member: GroupChatMember):
        try:
            command = text(
                """
                DELETE FROM group_chats_members
                WHERE group_chat_member_id = :group_chat_member_id
                """
            ).bindparams(group_chat_member_id=member.member.user_id)
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                connection.execute(command)
        except Exception as e:
            raise GroupChatMemberIsNotExist(f"{e}")

    @staticmethod
    def update(member: GroupChatMember):
        try:
            command = text(
                """
                UPDATE group_chats_members
                SET group_chat_member_id = :group_chat_member_id, group_chat_id = :group_chat_id, role = :role
                WHERE group_chat_member_id = :group_chat_member_id
                """
            ).bindparams(
                group_chat_member_id=member.member.user_id,
                group_chat_id=member.group_chat.group_chat_id,
                role=member.role
            )
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                connection.execute(command)
        except Exception as e:
            raise GroupChatMemberIsNotExist(f"{e}")

    @staticmethod
    async def with_id(member_id: UUID) -> GroupChatMember | None:
        try:
            query = text(
                """
                SELECT group_chat_member_id, group_chat_id, role
                FROM group_chats_members
                WHERE group_chat_member_id = :group_chat_member_id
                """
            ).bindparams(group_chat_member_id=member_id)
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                result = await connection.execute(query)
                row = result.fetchone()

            if not row:
                return None

            group_chat = GroupChatRepository.with_id(row.group_chat_id)
            member = UserRepository.with_id(row.group_chat_member_id)

            if isinstance(group_chat, GroupChat) and isinstance(member, User):
                return GroupChatMember(
                    group_chat=group_chat,
                    member=member,
                    role=row.role
                )
            else:
                return None
        except Exception as e:
            raise GroupChatMemberIsNotExist(f"{e}")
