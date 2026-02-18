import logging
import threading
from cre1_singleton_class import SingletonMeta


class AppLogger(metaclass=SingletonMeta):
    """
    Application logger singleton.
    Ensures logging is configured once. Use AppLogger.reset_instance() in tests.
    """

    def __init__(self, name: str = "myapp", level: int = logging.INFO):
        self._name = name
        self._level = level
        self._logger = logging.getLogger(name)
        self._configure_once()

    def _configure_once(self):
        # Only configure handlers once to avoid duplicate logs.
        if not getattr(self._logger, "_configured_by_app_logger", False):
            self._logger.setLevel(self._level)
            # Basic console handler with formatter
            ch = logging.StreamHandler()
            ch.setLevel(self._level)
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            ch.setFormatter(formatter)
            self._logger.addHandler(ch)
            # mark as configured
            setattr(self._logger, "_configured_by_app_logger", True)

    def get(self) -> logging.Logger:
        return self._logger

    @classmethod
    def reset_instance(cls) -> None:
        """Remove the singleton instance and remove custom config marker (useful for tests)."""
        with SingletonMeta._lock:
            inst = SingletonMeta._instances.pop(cls, None)
        if inst is not None:
            logger = logging.getLogger(inst._name)
            # Remove the marker so a new instance can reconfigure the logger
            if getattr(logger, "_configured_by_app_logger", False):
                delattr(logger, "_configured_by_app_logger")
                # Optionally clear handlers (careful in real apps)
                logger.handlers.clear()


# Demo / quick test
if __name__ == "__main__":
    # Get logger from singleton
    l1 = AppLogger().get()
    l2 = AppLogger().get()
    print("Same logger object:", l1 is l2)
    l1.info("This is an info log from the singleton logger")

    # Concurrency check
    loggers = []

    def make_logger():
        loggers.append(AppLogger().get())

    threads = [threading.Thread(target=make_logger) for _ in range(6)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    unique_logger_ids = {id(l) for l in loggers}
    print("Unique logger objects from threads:", unique_logger_ids)
    print("Only one unique logger across threads:", len(unique_logger_ids) == 1)
