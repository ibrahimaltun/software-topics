"""
Sometimes you want to register multiple prototypes and clone
them by name — like a “character factory”.
"""
import copy


class GameCharacter:
    def __init__(self, name, level, health, equipment=None, inventory=None):
        self.name = name
        self.level = level
        self.health = health
        self.equipment = equipment or {}
        self.inventory = inventory or []

    def __str__(self):
        return (f"Character: {self.name} (Level {self.level})\n"
                f"  Health: {self.health}\n"
                f"  Equipment: {self.equipment}\n"
                f"  Inventory: {self.inventory}")

    def clone(self):
        # Use deepcopy to clone all nested objects (lists, dicts, etc.)
        return copy.deepcopy(self)


class PrototypeRegistry:
    def __init__(self):
        self._prototypes = {}

    def register(self, name, prototype):
        self._prototypes[name] = prototype

    def unregister(self, name):
        del self._prototypes[name]

    def clone(self, prototype_name, **kwargs):
        prototype = self._prototypes.get(prototype_name)
        if not prototype:
            raise ValueError(f"Prototype '{prototype_name}' not found")

        cloned = prototype.clone()

        # Apply customizations
        for key, value in kwargs.items():
            setattr(cloned, key, value)

        return cloned


if __name__ == "__main__":
    # Create registry
    registry = PrototypeRegistry()

    # Register prototypes
    warrior = GameCharacter("Warrior", 10, 100, {
                            "sword": "Excalibur"}, ["potion"])
    mage = GameCharacter("Mage", 8, 80, {"staff": "Arcane"}, ["scroll"])

    registry.register("warrior", warrior)
    registry.register("mage", mage)

    # Clone and customize
    new_warrior = registry.clone("warrior", name="Hero", level=20, health=200)
    new_mage = registry.clone("mage", name="Sorcerer", level=15, health=120)

    print("New Warrior:")
    print(new_warrior)

    print("\n" + "="*50 + "\n")

    print("New Mage:")
    print(new_mage)
