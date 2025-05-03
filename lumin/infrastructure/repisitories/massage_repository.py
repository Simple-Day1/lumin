from typing import Type
from uuid import UUID
from sqlalchemy import text
from lumin.domain.massage.exceptions import MassageIsAlreadyExistError, MassageIsNotExistError
from lumin.domain.massage.massage import Massage
from lumin.infrastructure.database.config import PostgresConfig
from lumin.infrastructure.database.main import setup_engine, setup_connection


class MassageRepository:
    @staticmethod
    def add(massage: Massage) -> None:
        try:
            command = text(
                """
                INSERT INTO massages(massage_id, content, sender_id, recipient_id, timestamp, photo_urls, photo_id, video_id, status, reaction_id, fixed)
                VALUES :massage_id, :content, :sender_id, :recipient_id, :timestamp, :chat_id, :photo_urls, :video_urls, :status, :reaction_id, :fixed)
                """
            ).bindparams(
                massage_id=massage.massage_id,
                content=massage.content,
                sender_id=massage.sender_id,
                recipient_id=massage.recipient_id,
                timestamp=massage.timestamp,
                chat_id=massage.chat_id,
                photo_urls=massage.photo_urls,
                video_urls=massage.video_urls,
                status=massage.status,
                reaction_id=massage.reaction_id,
                fixed=massage.fixed
            )
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                connection.execute(command)
        except Exception as e:
            raise MassageIsAlreadyExistError(f"{e}")

    @staticmethod
    def delete(massage: Massage) -> None:
        try:
            command = text(
                """
                DELETE FROM massages
                WHERE massage_id = :massage_id
                """
            ).bindparams(massage_id=massage.massage_id)
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                connection.execute(command)
        except Exception as e:
            raise MassageIsNotExistError(f"{e}")

    @staticmethod
    def update(massage: Massage) -> None:
        try:
            command = text(
                """
                UPDATE massages
                SET massage_id = :massage_id, content = :content, sender_id = :sender_id, recipient_id = :recipient_id, timestamp = :timestamp, chat_id = :chat_id, photo_urls = :photo_urls, video_urls = :video_urls, status = :status, reaction_id = :reaction_id, fixed = :fixed
                WHERE massage_id = :massage_id
                """
            ).bindparams(
                massage_id=massage.massage_id,
                content=massage.content,
                sender_id=massage.sender_id,
                recipient_id=massage.recipient_id,
                timestamp=massage.timestamp,
                chat_id=massage.chat_id,
                photo_urls=massage.photo_urls,
                video_urls=massage.video_urls,
                status=massage.status,
                reaction_id=massage.reaction_id,
                fixed=massage.fixed
            )
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                connection.execute(command)
        except Exception as e:
            raise MassageIsNotExistError(f"{e}")

    @staticmethod
    async def with_id(massage_id: UUID) -> Massage | None:
        try:
            query = text(
                """
                SELECT massage_id, content, sender_id, recipient_id, timestamp, photo_urls, photo_id, video_id, status, reaction_id, fixed
                FROM massages
                WHERE massage_id = :massage_id
                """
            ).bindparams(massage_id=massage_id)
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                result = await connection.execute(query)
                row = result.fetchone()

            if not row:
                return None

            return Massage(
                massage_id=row.massage_id,
                content=row.content,
                sender_id=row.sender_id,
                recipient_id=row.recipient_id,
                timestamp=row.timestamp,
                chat_id=row.chat_id,
                photo_urls=row.photo_urls,
                video_urls=row.video_urls,
                status=row.status,
                reaction_id=row.reaction_id,
                fixed=row.fixed
            )
        except Exception as e:
            raise MassageIsNotExistError(f"{e}")
