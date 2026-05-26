"""Starting mini-game here."""

from random import randint as ri

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


monster = classes.Enemy(100, 10)

coins = 0
while True:
    print(f'Monster has {monster.hp} HP.')
    correct_answer = generate_math_problem()
    try:
        user_answer = int(input("Enter your answer: "))
    except ValueError:
        print("Error, invalid input")
        continue

    if user_answer == correct_answer:
        monster.take_damage(25)
        if not monster.is_alive:
            print(f"Monster has {monster.hp} HP.")
            print("Monster has been defeated")
            print(f"Monster dropped {monster.reward} coins.")
            coins += monster.reward
            print(f"You have {coins} coins.")
            break
    else:
        print(f"Uncorrect answer, must be {correct_answer}.")
