"""
Çok basit bir DI container.
Kayıt (register) ve çözümleme (resolve) sağlar;
singleton ve transient destekler; factory fonksiyon kayıt eder.
"""
from typing import Any, Callable, Dict, Type
import threading


class Lifetime:
    TRANSIENT = "transient"
    SINGLETON = "singleton"


class Registration:
    def __init__(self, factory: Callable[[], Any], lifetime: str):
        self.factory = factory
        self.lifetime = lifetime
        self._instance = None
        self._lock = threading.Lock()

    def resolve(self):
        if self.lifetime == Lifetime.TRANSIENT:
            return self.factory()
        # singleton
        if self._instance is None:
            with self._lock:
                if self._instance is None:
                    self._instance = self.factory()
        return self._instance


class Container:
    def __init__(self):
        self._registry: Dict[str, Registration] = {}

    def register(self, key: str, factory: Callable[[], Any], lifetime: str = Lifetime.TRANSIENT):
        if lifetime not in (Lifetime.TRANSIENT, Lifetime.SINGLETON):
            raise ValueError("Unsupported lifetime")
        self._registry[key] = Registration(factory, lifetime)

    def resolve(self, key: str):
        reg = self._registry.get(key)
        if reg is None:
            raise KeyError(f"No registration for key: {key}")
        return reg.resolve()

    # convenience: clear singletons (useful in tests)
    def clear_singletons(self):
        for reg in self._registry.values():
            reg._instance = None
