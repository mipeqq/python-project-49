import random, prompt
<<<<<<< HEAD
=======
from brain_games.cli import welcome_user
>>>>>>> 46f706c (Обновлены исключения; Добавлена игра brain-even; Пересобран пакет; Создана аскинема; создан скрипт brain-even.py)


def check_even(number):
    if number % 2 == 0:
<<<<<<< HEAD
      	return True
    else:
	    return False


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
=======
        return True
    else:
        return False

def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
>>>>>>> 46f706c (Обновлены исключения; Добавлена игра brain-even; Пересобран пакет; Создана аскинема; создан скрипт brain-even.py)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    countCorrect = 0
    num = 0

    while countCorrect < 3:
        num = random.randint(1,100)
        even = check_even(num)
        print('Question: ', num)
        ans = prompt.string('Answer: ')
        if ((even == True) and (ans == 'yes')) or ((even != True) and (ans == 'no')):
<<<<<<< HEAD
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
=======
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

>>>>>>> 46f706c (Обновлены исключения; Добавлена игра brain-even; Пересобран пакет; Создана аскинема; создан скрипт brain-even.py)
if __name__ == '__main__':
    main()
