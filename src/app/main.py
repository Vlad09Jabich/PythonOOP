"""Starting mini-game here."""

from random import randint as ri
from random import choice

import classes


def calculate_correct_answer(f_op: int, s_op: int) -> int:
    """Return correct answer."""
    return f_op + s_op


def generate_math_problem() -> int:
    """Generate all numbers, print the question and return correct answer."""
    f_op = ri(0, 100)
    s_op = ri(0, 100)
    print("Solve this problem to dealt damage:")
    print(f"{f_op} + {s_op} = ?")
    return calculate_correct_answer(f_op, s_op)


def summon_new_monster():
    """Summon random enemy instance"""
    return choice([summon_elite_enemy, summon_enemy])()


def summon_elite_enemy():
    """Return new EliteEnemy instance."""
    return classes.EliteEnemy(100, 0.2, 25)


def summon_enemy():
    """Return new Enemy instance."""
    return classes.Enemy(50, 10)


current_monster = classes.Enemy(50, 10)

coins = 0
while True:
    print(f'\nMonster has {current_monster.hp} HP.')
    correct_answer = generate_math_problem()
    try:
        user_answer = int(input("Enter your answer: "))
    except ValueError:
        print("Error, invalid input")
        continue

    if user_answer == correct_answer:
        current_monster.take_damage(25)
        if not current_monster.is_alive:
            print(f"Monster has {current_monster.hp} HP.")
            print("Monster has been defeated")
            print(f"Monster dropped {current_monster.reward} coins.")
            coins += current_monster.reward
            print(f"You have {coins} coins.")
            current_monster = summon_new_monster()
    else:
        print(f"Uncorrect answer, must be {correct_answer}.")
