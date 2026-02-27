from collections import defaultdict


class EventBus:
    """Publisher/Subscribe IoC"""

    def __init__(self):
        self._subs = defaultdict(list)

    def subscribe(self, event_name, handler):
        self._subs[event_name].append(handler)

    def publish(self, event_name, payload):
        for handler in self._subs[event_name]:
            handler(payload)


def on_user_created(payload):
    print("Send welcome email to", payload["email"])


def on_user_created_audit(payload):
    print("Audit log:", payload["id"], payload["email"])


if __name__ == "__main__":
    bus = EventBus()
    bus.subscribe("user.created", on_user_created)
    bus.subscribe("user.created", on_user_created_audit)

    # Bir yerlerde user oluşturuldu; event publish eden taraf:
    bus.publish("user.created", {"id": 1, "email": "alice@example.com"})
