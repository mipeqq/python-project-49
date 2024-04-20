from brain_games.cli import welcome_user
from brain_games.common_logic import check_answer
import random
import prompt


def is_prime(number):
    if number <= 1:
        return 'no'

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return 'no'

    return 'yes'


def game_prime():
    countCorrect = 0
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while countCorrect <= 3:
        num = random.randint(1, 51)
        print(f'Question: {num}')
        result = is_prime(num)
        ans = prompt.string('Your answer: ')
        if check_answer(ans, result):
            countCorrect += 1
        else:
            print(f"Let's try again, {name}!")
            break

        if countCorrect == 3:
            print(f'Congratulations, {name}!')
            break
