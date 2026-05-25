"""Starting mini-game here."""

from classes import Enemy

monster = Enemy(100)

attack = None
while True:
    print(f"Monster has {monster.hp} HP.")

    attack = int(input("Enter damage for enemy: "))
    monster.take_damage(attack)

    if not monster.is_alive:
        print(f"Monster has {monster.hp} HP.")
        print("Monster has been defeated")
        break
