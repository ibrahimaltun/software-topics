import json
import threading
from typing import Any, Optional


class SingletonMeta(type):
    """Thread-safe Singleton metaclass."""
    _instances: dict = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        # Fast path
        if cls in cls._instances:
            return cls._instances[cls]
        # Slow path with lock
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Config(metaclass=SingletonMeta):
    """
    Configuration manager singleton.
    Loads JSON from a file on creation and provides read access.
    Use Config.reset_instance() in tests to drop the singleton and reinitialize.
    """

    def __init__(self, path: str = "config.json"):
        self._path = path
        self._data = {}
        self._load()

    def _load(self) -> None:
        try:
            with open(self._path, "r", encoding="utf-8") as f:
                self._data = json.load(f)
        except FileNotFoundError:
            self._data = {}
        except json.JSONDecodeError:
            # Keep empty dict on parse error (or raise if you prefer)
            self._data = {}

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        return self._data.get(key, default)

    def reload(self) -> None:
        """Reload configuration from disk."""
        self._load()

    @classmethod
    def reset_instance(cls) -> None:
        """Remove the singleton instance (useful for tests)."""
        with SingletonMeta._lock:
            SingletonMeta._instances.pop(cls, None)


# Demo / quick test
if __name__ == "__main__":
    # Create two references and prove they are the same instance
    c1 = Config("1.cre_backend_config.json")
    # second creation returns the same instance (path ignored)
    c2 = Config("1.cre_frontend_config.json")

    print("Same instance:", c1 is c2)
    print("Config example:", c1.get("app_name", "unknown"))

    # Concurrency check: instantiate from several threads
    instances = []

    def make_config():
        instances.append(Config())

    threads = [threading.Thread(target=make_config) for _ in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    unique_ids = {id(i) for i in instances}
    print("Instances created in threads (unique ids):", unique_ids)
    print("Only one unique instance across threads:", len(unique_ids) == 1)
