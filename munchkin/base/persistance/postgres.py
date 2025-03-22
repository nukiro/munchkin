from logging import info
from typing import Any, Optional, Self, Sequence, TypedDict

from psycopg import Connection, Cursor, connect

type PostgresConnection = Connection


class PostgresConfiguration(TypedDict):
    host: str
    port: str
    database: str
    username: str
    password: str


class DictRowFactory:
    def __init__(self, cursor: Cursor[Any]):
        self.fields = [c.name for c in cursor.description]

    def __call__(self, values: Sequence[Any]) -> dict[str, Any]:
        return dict(zip(self.fields, values))


class Postgres:
    def __init__(
        self,
        config: Optional[PostgresConfiguration] = dict(
            host="127.0.0.1",
            port="5432",
            database="dev",
            username="munchkin",
            password="munchkin",
        ),
    ):
        self._config: PostgresConfiguration = config
        self._conn: PostgresConnection = None

    def connect(self) -> Self:
        conn_path = (
            f"postgres://"
            f"{self._config.get('username')}:{self._config.get('password')}"
            "@"
            f"{self._config.get('host')}:{self._config.get('port')}"
            "/"
            f"{self._config.get('database')}"
        )

        # it will raise an exception if there is any error connecting to the database
        self._conn = connect(
            conninfo=conn_path, row_factory=DictRowFactory, autocommit=False
        )

        info("Configured and connected to the database.")

        return self

    def disconnect(self):
        self._conn.close()

        if not self._conn.closed:
            raise RuntimeError(
                "The postgres database connection was not closed successfully."
            )
