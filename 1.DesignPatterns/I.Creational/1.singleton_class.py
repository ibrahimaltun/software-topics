import threading


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
