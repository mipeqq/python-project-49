from brain_games.cli import welcome_user
import random, prompt


def check_sign_and_answer(sign):
    if sign == 0:
        print('Question')


def check_answer(answer,result):
    if answer == result:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
        print("Let's try again!")
        return False

def main():
    sign = 0                         # 0 - +;   1 - -;   2 - *
    num1 = 0
    num2 = 0
    num3 = 0                         # это будет однозначное число, для упрощения умножения
    name = welcome_user()
    print('What is the result of the expression?')
    while sign < 3:
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        num3 = random.randint(1,11)
        if sign == 0:
            print(f'Question: {num1} + {num2}')
            ans = prompt.integer('Answer: ')
            result = num1 + num2
            if check_answer(ans,result):
                sign += 1
                continue
            else:
                break
        if sign == 1:
            print(f'Question: {num1} - {num2}')
            ans = prompt.integer('Answer: ')
            result = num1 - num2
            if check_answer(ans,result):
                sign += 1
                continue
            else:
                break
        if sign == 2:
            print(f'Question: {num1} * {num3}')
            ans = prompt.integer('Answer: ')
            result = num1 * num3
            if check_answer(ans,result):
                sign += 1
                continue
            else:
                break
    
    if sign == 3:
        print(f"Congratulations!")

            
if __name__ == '__main__':
    main()



        
