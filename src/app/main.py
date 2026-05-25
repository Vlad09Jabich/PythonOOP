from random import randint


class Enemy:
    def __init__(self, hp: int):
        self.hp = hp

    def damage_taken(self, damage: int):
        self.hp = max(0, self.hp - damage)

    @property
    def is_alive(self) -> bool:
        return self.hp > 0


monster = Enemy(100)

attack = None
while True:
    print(f"Monster has {monster.hp} HP.")

    attack = int(input("Enter damage for enemy: "))
    monster.damage_taken(attack)

    if not monster.is_alive:
        print(f"Monster has {monster.hp} HP.")
        print("Monster has been defeated")
        break