from typing import Type
from uuid import UUID
from sqlalchemy import text
from lumin.domain.personal_chat_member.personal_chat_member import PersonalChatMember
from lumin.domain.personal_chat_member.exceptions import PersonalChatMemberIsNotExist, PersonalChatMemberIsAlreadyExist
from lumin.domain.personal_сhat.personal_chat import PersonalChat
from lumin.domain.user.user import User
from lumin.infrastructure.database.config import PostgresConfig
from lumin.infrastructure.database.main import setup_engine, setup_connection
from lumin.infrastructure.repisitories.personal_chat_repository import PersonalChatRepository
from lumin.infrastructure.repisitories.user_repository import UserRepository


class PersonalChatMemberRepository:
    @staticmethod
    def add(member: PersonalChatMember) -> None:
        try:
            command = text(
                """
                INSERT INTO personal_chats_members(personal_chat_member_id, personal_chat_id, role)
                VALUES :personal_chat_member_id, :personal_chat_id, :role
                """
            ).bindparams(
                personal_chat_member_id=member.member.user_id,
                personal_chat_id=member.personal_chat.personal_chat_id,
                role=member.role
            )
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                connection.execute(command)
        except Exception as e:
            raise PersonalChatMemberIsAlreadyExist(f"{e}")

    @staticmethod
    def delete(member: PersonalChatMember) -> None:
        try:
            command = text(
                """
                DELETE FROM personal_chats_members
                WHERE personal_chat_member_id = :personal_chat_member_id
                """
            ).bindparams(personal_chat_member_id=member.member.user_id)
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                connection.execute(command)
        except Exception as e:
            raise PersonalChatMemberIsNotExist(f"{e}")

    @staticmethod
    def update(member: PersonalChatMember) -> None:
        try:
            command = text(
                """
                UPDATE personal_chats_members
                SET personal_chat_member_id = :personal_chat_member_id, personal_chat_id = :personal_chat_id, role = :role
                WHERE personal_chat_member_id = :personal_chat_member_id
                """
            ).bindparams(
                personal_chat_member_id=member.member.user_id,
                personal_chat_id=member.personal_chat.personal_chat_id,
                role=member.role
            )
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                connection.execute(command)
        except Exception as e:
            raise PersonalChatMemberIsNotExist(f"{e}")

    @staticmethod
    async def with_id(member_id: UUID) -> PersonalChatMember | None:
        try:
            query = text(
                """
                SELECT personal_chat_member_id, personal_chat_id, role
                FROM personal_chats_members
                WHERE personal_chat_member_id = :personal_chat_member_id
                """
            ).bindparams(group_chat_member_id=member_id)
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                result = await connection.execute(query)
                row = result.fetchone()

            if not row:
                return None

            personal_chat = PersonalChatRepository.with_id(row.group_chat_id)
            member = UserRepository.with_id(row.group_chat_member_id)

            if isinstance(personal_chat, PersonalChat) and isinstance(member, User):
                return PersonalChatMember(
                    group_chat=personal_chat,
                    member=member,
                    role=row.role
                )
            else:
                return None
        except Exception as e:
            raise PersonalChatMemberIsNotExist(f"{e}")
