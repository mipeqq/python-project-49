from brain_games.cli import welcome_user
from brain_games.common_logic import check_answer
import prompt
import random


def check_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def game_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    countCorrect = 0
    num = 0

    while countCorrect < 3:
        num = random.randint(1, 100)
        even = check_even(num)
        print(f'Question: {num}')
        ans = prompt.string('Answer: ')
        if check_answer(ans, even):
            countCorrect += 1
        else:
            print(f"Let's try again, {name}!")
            break

    if countCorrect == 3:
        print(f"Congratulations, {name}!")
