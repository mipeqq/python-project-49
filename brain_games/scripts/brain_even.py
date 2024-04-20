import random, prompt
from brain_games.cli import welcome_user


def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    countCorrect = 0
    num = 0

    while countCorrect < 3:
        num = random.randint(1,100)
        even = check_even(num)
        print('Question: ', num)
        ans = prompt.string('Answer: ')
        if ((even == True) and (ans == 'yes')) or ((even != True) and (ans == 'no')):
            print('Correct!')
            countCorrect += 1
        else:
            if (even == True):
                print(f'"{ans}" is wrong answer ;(. Correct answer is "yes".')
                print(f"Let's try again, {name}!")
                break
            else:
                print(f'"{ans}" is wrong answer ;(. Correct answer is "no".')
                print(f"Let's try again, {name}!")
                break

    if countCorrect == 3:
        print(f"Congratulations, {name}!")

if __name__ == '__main__':
    main()
