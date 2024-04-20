from brain_games.cli import welcome_user
import random
import prompt


def GCD(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a


def check_answer(answer, result):
    if answer == result:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
        return False


def main():
    countCorrect = 0
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    while countCorrect <= 3:
        num1 = random.randint(1, 101)
        num2 = random.randint(1, 101)
        while GCD(num1, num2) == 1:  # чтобы убрать частый ответ 1
            num1 = random.randint(1, 101)
            num2 = random.randint(1, 101)
        print(f"Question: {num1} {num2}")
        ans = prompt.integer('Answer: ')
        result = GCD(num1, num2)
        if check_answer(ans, result):
            countCorrect += 1
        else:
            print(f"Let's try again, {name}")
            break

        if countCorrect == 3:
            print(f"Congratulations, {name}!")
            break


if __name__ == '__main__':
    main()
