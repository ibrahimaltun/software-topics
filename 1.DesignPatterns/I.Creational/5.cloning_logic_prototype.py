"""
Prototype Pattern = Clone existing objects instead of creating from scratch
Avoids expensive object creation
Enables customization after cloning
Use when you have complex objects that are expensive to create
Python’s copy.deepcopy() makes it easy to implement

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


if __name__ == "__main__":
    # Create a prototype character
    original = GameCharacter(
        name="Warrior",
        level=10,
        health=100,
        equipment={"sword": "Excalibur", "shield": "Aegis"},
        inventory=["potion", "key"]
    )

    print("Original Character:")
    print(original)

    print("\n" + "="*50 + "\n")

    # Clone it
    cloned = original.clone()

    # Customize the clone
    cloned.name = "Warrior Clone"
    cloned.level = 15
    cloned.health = 150
    cloned.equipment["armor"] = "Dragon Scale"
    cloned.inventory.append("map")

    print("Cloned Character (customized):")
    print(cloned)

    print("\n" + "="*50 + "\n")

    # Verify they are different objects
    print("Original and Clone are different objects:", original is not cloned)
    print("Original and Clone have different names:",
          original.name != cloned.name)
    print("Original and Clone have different equipment:",
          original.equipment != cloned.equipment)
