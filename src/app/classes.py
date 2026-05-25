"""Defines classes."""

class Enemy:
    """Defines the base attributes and behavior of a standard enemy."""
    def __init__(self, hp: int, reward: int):
        """Create an enemy instance with a specified amount of health."""
        self.hp = hp
        self.reward = reward

    def take_damage(self, damage: float) -> None:
        """Handle damage calculation and reduce enemy health."""
        self.hp = round(max(0, self.hp - damage), 1)

    @property
    def is_alive(self) -> bool:
        """Check if the enemy is alive."""
        return self.hp > 0


class EliteEnemy (Enemy):
    """Defines attributes and behavior of an elite enemy."""
    def __init__(self, hp: int, armor: float, reward: int):
        """Create an elite enemy instance"""
        super().__init__(hp, reward)
        self.armor = armor

    def take_damage(self, damage: float):
        """Calculate damage reduction then applying."""
        damage_block = round(damage * self.armor, 1)
        final_damage = max(0, damage - damage_block)

        print(f"Elite monster block {damage_block} damage.")
        super().take_damage(final_damage)
