import asyncio

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text
from tables import metadata


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL_asyncpg(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    @property
    def DATABASE_URL_psycopg(self):
        return f'postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    model_config = SettingsConfigDict(env_file="../../../.env")


settings = Settings()

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True,
    pool_size=5,
    max_overflow=10
)

sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    pool_size=5,
    max_overflow=10
)


async def setup_async_connection():
    async with async_engine.connect() as connection:
        res = await connection.execute(text("SELECT VERSION()"))
        print(f'{res.first()=}')


def setup_sync_connection():
    with sync_engine.connect() as connection:
        res = connection.execute(text("SELECT VERSION()"))
        print(f'{res.first()=}')


def sync_create_tables():
    metadata.create_all(sync_engine)


def insert_data():
    with setup_sync_connection() as connection:
        stmt = """INSERT INTO users (username) VALUES
        ('a')"""


if __name__ == '__main__':
    #asyncio.run(setup_async_connection())
    setup_sync_connection()
    sync_create_tables()
