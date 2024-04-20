from brain_games.cli import welcome_user
from brain_games.common_logic import check_answer
import random
import prompt


def game_calc():
    countCorrect = 0   # 0 - +;   1 - -;   2 - *
    num1 = 0
    num2 = 0
    num3 = 0   # это будет однозначное число, для упрощения умножения
    name = welcome_user()
    print('What is the result of the expression?')
    while countCorrect <= 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        num3 = random.randint(1, 11)
        match countCorrect:
            case 0:
                print(f'Question: {num1} + {num2}')
                ans = prompt.integer('Answer: ')
                result = num1 + num2
                if check_answer(ans, result):
                    countCorrect += 1
                else:
                    print(f"Let's try again, {name}")
                    break
            case 1:
                print(f'Question: {num1} - {num2}')
                ans = prompt.integer('Answer: ')
                result = num1 - num2
                if check_answer(ans, result):
                    countCorrect += 1
                else:
                    print(f"Let's try again, {name}")
                    break
            case 2:
                print(f'Question: {num1} * {num3}')
                ans = prompt.integer('Answer: ')
                result = num1 * num3
                if check_answer(ans, result):
                    countCorrect += 1
                else:
                    print(f"Let's try again, {name}!")
                    break
            case 3:
                print(f"Congratulations, {name}!")
                break
