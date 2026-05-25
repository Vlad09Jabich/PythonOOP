"""Defines classes."""

class Enemy:
    """Defines the base attributes and behavior of a standard enemy."""
    def __init__(self, hp: int):
        """Create an enemy instance with a specified amount of health."""
        self.hp = hp

    def take_damage(self, damage: int):
        """Handle damage calculation and reduce enemy health."""
        self.hp = max(0, self.hp - damage)

    @property
    def is_alive(self) -> bool:
        """Check if the enemy is alive."""
        return self.hp > 0
