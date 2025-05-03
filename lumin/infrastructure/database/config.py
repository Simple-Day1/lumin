from dataclasses import dataclass, field


@dataclass(frozen=True)
class PostgresConfig:
    host: str = field(default="localhost")
    port: int = field(default=5432)
    user: str = field(default="some_user")
    password: str = field(default="some_user")
    database: str = field(default="testdb")
    echo: bool = field(default=False)

    @property
    def postgres_dsn(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
