"""Starting mini-game here."""

from random import randint
import classes

monster = classes.EliteEnemy(100, 0.2, randint(10, 25))

coins = 0

while True:
    print(f"Monster has {monster.hp} HP.")

    attack = float(input("Enter damage for enemy: "))
    monster.take_damage(attack)

    if not monster.is_alive:
        print(f"Monster has {monster.hp} HP.")
        print("Monster has been defeated")
        print(f"Monster dropped {monster.reward} coins.")
        coins += monster.reward
        print(f"You have {coins} coins.")
        break
