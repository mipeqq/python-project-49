from brain_games.cli import welcome_user
from brain_games.common_logic import check_answer
import prompt
import random


def gen_progression():
    length = random.randint(5, 13)
    step_progression = random.randint(2, 11)
    first_number = random.randint(1, 51)
    progression = []
    progression.append(str(first_number))
    for i in range(0, length - 1):
        last_num = progression[-1]
        progression.append(str(int(last_num) + step_progression))
    return progression


def hide_num(progression):
    length = len(progression)
    index = random.randint(0, length - 1)
    result = progression[index]
    progression[index] = '..'
    hide_progression = progression
    final_progression = ' '.join(hide_progression)
    return final_progression, result


def game_progression():
    countCorrect = 0
    name = welcome_user()
    print('What number is missing in the progression?')
    while countCorrect <= 3:
        start_progression = gen_progression()
        hide_progression, result = hide_num(start_progression)
        print(f"Question: {hide_progression}")
        ans = prompt.string('Answer: ')
        if check_answer(ans, result):
            countCorrect += 1
        else:
            print(f"Let's try again, {name}!")
            break
        if countCorrect == 3:
            print(f"Congratulations, {name}!")
            break
