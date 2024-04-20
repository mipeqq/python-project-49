import random
import prompt
from brain_games.cli import welcome_user


def check_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def check_answer(answer, result):
    if answer == result:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
        return False


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    countCorrect = 0
    num = 0

    while countCorrect < 3:
        num = random.randint(1, 100)
        even = check_even(num)
        print('Question: ', num)
        ans = prompt.string('Answer: ')
        if check_answer(ans, even):
            countCorrect += 1
        else:
            print(f"Let's try again, {name}!")
            break

    if countCorrect == 3:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
