"""
db_connection_factory.py
Basit Factory: konfigürasyona göre uygun DB connector nesnesini döner.
"""
from abc import ABC, abstractmethod
from typing import Dict, Any


# --- Common interface for DB connectors ---
class DBConnection(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def execute(self, query: str) -> Any:
        pass

    @abstractmethod
    def close(self) -> None:
        pass


# --- Concrete connectors (mock implementations for demo) ---
class SQLiteConnection(DBConnection):
    def __init__(self, path: str):
        self.path = path
        self._connected = False

    def connect(self) -> None:
        self._connected = True
        print(f"[SQLite] connected to {self.path}")

    def execute(self, query: str) -> Any:
        if not self._connected:
            raise RuntimeError("Not connected")
        print(f"[SQLite] executing: {query}")
        return "sqlite-result"

    def close(self) -> None:
        self._connected = False
        print("[SQLite] closed")


class PostgresConnection(DBConnection):
    def __init__(self, dsn: str):
        self.dsn = dsn
        self._connected = False

    def connect(self) -> None:
        self._connected = True
        print(f"[Postgres] connected to {self.dsn}")

    def execute(self, query: str) -> Any:
        if not self._connected:
            raise RuntimeError("Not connected")
        print(f"[Postgres] executing: {query}")
        return "postgres-result"

    def close(self) -> None:
        self._connected = False
        print("[Postgres] closed")


# --- Factory (Simple Factory) ---
class ConnectionFactory:
    @staticmethod
    def get_connection(config: Dict[str, Any]) -> DBConnection:
        """
        config example:
          {"type": "sqlite", "path": "data.db"}
          {"type": "postgres", "dsn": "postgres://user:pass@host/db"}
        """
        db_type = config.get("type")
        if db_type == "sqlite":
            return SQLiteConnection(path=config["path"])
        elif db_type == "postgres":
            return PostgresConnection(dsn=config["dsn"])
        else:
            raise ValueError(f"Unknown db type: {db_type}")


# --- Demo usage ---
if __name__ == "__main__":
    # Imagine this comes from app config
    cfg_sqlite = {"type": "sqlite", "path": "app.db"}
    cfg_pg = {"type": "postgres", "dsn": "postgres://user:pass@localhost/db"}

    # Client code does not depend on concrete classes
    conn = ConnectionFactory.get_connection(cfg_sqlite)
    conn.connect()
    print("Query result:", conn.execute("SELECT 1"))
    conn.close()

    print("--- switch to postgres via same client code ---")
    conn2 = ConnectionFactory.get_connection(cfg_pg)
    conn2.connect()
    print("Query result:", conn2.execute("SELECT now()"))
    conn2.close()
