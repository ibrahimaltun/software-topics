"""
Arayüzler (Protocol), concrete sınıflar (Repository, Service), 
controller ve container ile wiring.
Hem manuel wiring hem container wiring gösterir.
"""
from typing import Protocol, List
from s_di_container import Container, Lifetime


class User:
    """User Interface"""

    def __init__(self, user_id: int, name: str):
        self.id = user_id
        self.name = name


class IUserRepository(Protocol):
    def get_user(self, user_id: int) -> User:
        ...

    def list_users(self) -> List[User]:
        ...


class IUserService(Protocol):
    def greet_user(self, user_id: int) -> str:
        ...


class InMemoryUserRepository:
    """Concrete implementations"""

    def __init__(self):
        self._data = {
            1: User(1, "Alice"),
            2: User(2, "Bob"),
        }

    def get_user(self, user_id: int) -> User:
        return self._data.get(user_id)

    def list_users(self):
        return list(self._data.values())


class GreetingService:
    def __init__(self, user_repo: IUserRepository):
        self._repo = user_repo

    def greet_user(self, user_id: int) -> str:
        user = self._repo.get_user(user_id)
        if user:
            return f"Hello, {user.name}!"
        return "User not found"


def manual_demo():
    """Manual wiring (no container)"""
    repo = InMemoryUserRepository()
    svc = GreetingService(repo)
    print(svc.greet_user(1))
    print(svc.greet_user(42))


def container_demo():
    """Container wiring demo"""
    c = Container()
    # register repo as singleton (one shared repo)
    c.register("user_repo", lambda: InMemoryUserRepository(),
               lifetime=Lifetime.SINGLETON)
    # register service as transient (new instance on every resolve), but factory pulls repo from container
    c.register("greeting_service", lambda: GreetingService(
        c.resolve("user_repo")), lifetime=Lifetime.TRANSIENT)

    svc1 = c.resolve("greeting_service")
    svc2 = c.resolve("greeting_service")
    print("svc1 is svc2:", svc1 is svc2)  # False because transient
    print(svc1.greet_user(2))
    print(svc2.greet_user(99))


if __name__ == "__main__":
    print("--- manual demo ---")
    manual_demo()
    print("\n--- container demo ---")
    container_demo()
