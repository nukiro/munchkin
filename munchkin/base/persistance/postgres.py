from logging import info
from typing import Optional, Self, TypedDict

from psycopg import Connection
from psycopg import connect as connect_postgres

from munchkin.base.persistance.repository import SqlDictRowFactory

type PostgresConnection = Connection


class PostgresConfiguration(TypedDict):
    host: str
    port: str
    database: str
    username: str
    password: str


class Postgres:
    def __init__(
        self,
        config: Optional[PostgresConfiguration] = dict(
            host="127.0.0.1",
            port="5432",
            database="munchkin-local",
            username="munchkin",
            password="munchkin",
        ),
    ):
        self._config: PostgresConfiguration = config
        self._conn: Optional[PostgresConnection] = None

    def connect(self) -> Self:
        if self._conn:
            raise ValueError("Database is already connected.")

        conn_path = (
            f"postgres://"
            f"{self._config.get('username')}:{self._config.get('password')}"
            "@"
            f"{self._config.get('host')}:{self._config.get('port')}"
            "/"
            f"{self._config.get('database')}"
        )

        # it will raise an exception if there is any error connecting to the database
        self._conn = connect_postgres(
            conninfo=conn_path, row_factory=SqlDictRowFactory, autocommit=False
        )

        info("Configured and connected to the database.")

        return self

    def disconnect(self):
        if not self._conn:
            raise ValueError("There is no active connection.")

        self._conn.close()

        if not self._conn.closed:
            raise RuntimeError(
                "The postgres database connection was not closed successfully."
            )

        # clear connection data
        self._conn = None

        info("Disconnected from Postgres.")
