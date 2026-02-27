"""Constructor injection"""
from typing import Protocol


class IMessageSender(Protocol):
    def send(self, to: str, msg: str) -> None: ...


class EmailSender:
    def send(self, to: str, msg: str) -> None:
        print(f"[Email] to={to}: {msg}")


class NotificationService:
    # NotificationService, IMessageSender bağımlılığını oluşturmaz; dışarıdan alır (injected)
    def __init__(self, sender: IMessageSender):
        self._sender = sender

    def notify(self, user_email: str, text: str):
        self._sender.send(user_email, text)


if __name__ == "__main__":
    # Wiring kodu (main / composition root): kim hangi implementasyonu verecek burada belirlenir
    sender = EmailSender()
    svc = NotificationService(sender)
    svc.notify("bob@example.com", "Hello via DI")
    