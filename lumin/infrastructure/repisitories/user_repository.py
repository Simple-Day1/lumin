from typing import Type
from uuid import UUID
from sqlalchemy import text
from lumin.infrastructure.database.config import PostgresConfig
from lumin.domain.user.exceptions import UserIsNotExistError, UserIsAlreadyExistError
from lumin.domain.user.user import User
from lumin.domain.user.value_objects import Phone, Date
from lumin.infrastructure.database.main import setup_engine, setup_connection


class UserRepository:
    @staticmethod
    def add(user: User) -> None:
        try:
            command = text(
                """
                INSERT INTO users(user_id, username, email, description, phone, date, user_avatar_url)
                VALUES :user_id, :username, :email, :description, :phone, :date, :user_avatar_url
                """
            ).bindparams(
                user_id=user.user_id,
                username=user.username,
                email=user.email,
                description=user.description,
                phone=user.phone,
                date=user.date,
                user_avatar_url=user.user_avatar_url
            )
            engine = setup_engine(Type[PostgresConfig])
            with setup_connection(engine) as connection:
                connection.execute(command)
        except Exception as e:
            raise UserIsAlreadyExistError(f"{e}")

    @staticmethod
    def delete(user: User) -> None:
        query = text(
            """
            DELETE FROM users
            WHERE user_id = :user_id
            """
        ).bindparams(
            user_id=user.user_id,
            username=user.username,
            email=user.email,
            description=user.description,
            phone=user.phone,
            date=user.date,
            user_avatar_url=user.user_avatar_url
        )

        engine = setup_engine(Type[PostgresConfig])
        with setup_connection(engine) as connection:
            connection.execute(query)

    @staticmethod
    def update(user: User) -> None:
        query = text(
            """
            UPDATE massages
            SET user_id = :user_id, username = :username, email = :email, description = :description, phone = :phone, date = :date, user_avatar_url = :user_avatar_url
            WHERE massage_id = :massage_id
            """
        ).bindparams(
            user_id=user.user_id,
            username=user.username,
            email=user.email,
            description=user.description,
            phone=user.phone,
            date=user.date,
            user_avatar_url=user.user_avatar_url
        )

        engine = setup_engine(Type[PostgresConfig])
        with setup_connection(engine) as connection:
            connection.execute(query)

    @staticmethod
    async def with_id(user_id: UUID) -> User | None:
        query = text(
            """
            SELECT user_id, username, email, description, phone, date, user_avatar_url
            FROM users
            WHERE user_id = :user_id
            """
        ).bindparams(user_id=user_id)
        engine = setup_engine(Type[PostgresConfig])
        with setup_connection(engine) as connection:
            result = await connection.execute(query)
            row = result.fetchone()

        if not row:
            return None

        return User(
            user_id=row.user_id,
            username=row.username,
            description=row.description,
            phone=Phone(phone=row.phone),
            date=Date(date=row.date),
            user_avatar_url=row.user_avatar_url,
        )
