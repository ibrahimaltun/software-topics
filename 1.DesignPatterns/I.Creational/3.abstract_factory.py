"""
notification_abstract_factory.py
Abstract Factory örneği: farklı notification kanalları (Email, SMS) için
ilgili Sender ve Formatter çiftlerini üretir.
Çalıştırma: python notification_abstract_factory.py
"""
from abc import ABC, abstractmethod
from typing import Protocol, Dict


# --- Abstract product interfaces ---
class MessageFormatter(ABC):
    @abstractmethod
    def format(self, payload: Dict) -> str:
        pass


class MessageSender(ABC):
    @abstractmethod
    def send(self, to: str, message: str) -> bool:
        pass


# --- Concrete products for Email ---
class EmailFormatter(MessageFormatter):
    def format(self, payload: Dict) -> str:
        # simple templating
        return f"Subject: {payload.get('subject')}\n\n{payload.get('body')}"


class EmailSender(MessageSender):
    def send(self, to: str, message: str) -> bool:
        # mock sending
        print(f"[EmailSender] Sending email to {to}:\n{message}")
        return True


# --- Concrete products for SMS ---
class SMSFormatter(MessageFormatter):
    def format(self, payload: Dict) -> str:
        # SMS: short text only
        return f"{payload.get('body')}"


class SMSSender(MessageSender):
    def send(self, to: str, message: str) -> bool:
        # mock sending
        print(f"[SMSSender] Sending SMS to {to}: {message}")
        return True


# --- Abstract factory interface ---
class NotificationFactory(ABC):
    @abstractmethod
    def create_formatter(self) -> MessageFormatter:
        pass

    @abstractmethod
    def create_sender(self) -> MessageSender:
        pass


# --- Concrete factories ---
class EmailNotificationFactory(NotificationFactory):
    def create_formatter(self) -> MessageFormatter:
        return EmailFormatter()

    def create_sender(self) -> MessageSender:
        return EmailSender()


class SMSNotificationFactory(NotificationFactory):
    def create_formatter(self) -> MessageFormatter:
        return SMSFormatter()

    def create_sender(self) -> MessageSender:
        return SMSSender()


# --- Client code that uses the abstract factory ---
class NotificationService:
    def __init__(self, factory: NotificationFactory):
        self._factory = factory
        self._formatter = factory.create_formatter()
        self._sender = factory.create_sender()

    def notify(self, to: str, payload: Dict) -> bool:
        message = self._formatter.format(payload)
        return self._sender.send(to, message)


# --- Demo usage ---
if __name__ == "__main__":
    email_factory = EmailNotificationFactory()
    sms_factory = SMSNotificationFactory()

    payload = {"subject": "Welcome", "body": "Hello Alice, welcome aboard!"}

    svc_email = NotificationService(email_factory)
    svc_email.notify("alice@example.com", payload)

    svc_sms = NotificationService(sms_factory)
    svc_sms.notify("+1234567890", payload)
