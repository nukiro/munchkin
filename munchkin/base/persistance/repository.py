from abc import ABC, abstractmethod
from logging import debug
from typing import List, Optional, TypedDict

from munchkin.base.persistance.postgres import Postgres

type UUID = str


class Schema(TypedDict):
    """Represent table schema common attributes for all tables in the repository."""

    _uuid: Optional[UUID]


class IRepository[T: Schema](ABC):
    """
    Repository interface defining persistance operations.

    It manages CRUD (Create, Read, Update, Delete) operations and interacts with data sources like SQL or NoSQL databases, files, etc. All the implementations have to implement these operations.
    """

    @abstractmethod
    def get(self) -> List[T]:
        pass


class SqlRepository[T: Schema](IRepository):
    def __init__(self, database: Postgres, tablename):
        # first check if the database is connected
        if not database._conn:
            raise ValueError("Database is not connected yet.")

        self._db = database
        self._data_table = tablename
        self._audit_table = f"_{tablename}"

    def get(self) -> List[T]:
        sql = f"SELECT * FROM {self._data_table}"
        debug(sql)

        cur = self._db._conn.cursor()
        cur.execute(sql)

        results: List[T] = cur.fetchall()
        return results
