from typing import AsyncGenerator
from psycopg import AsyncConnection
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from lumin.infrastructure.database.config import PostgresConfig


async def setup_engine(config: PostgresConfig) -> AsyncEngine | None:
    engine = create_async_engine(
        config.postgres_dsn,
        echo=config.echo,
    )
    yield engine

    await engine.dispose()


async def setup_connection(engine: AsyncEngine) -> AsyncConnection | None:
    async with engine.begin() as connection:
        yield connection
