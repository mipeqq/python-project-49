def check_answer(answer, result):
    if answer == result:
        print('Correct!')
        return True

    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
        return False
