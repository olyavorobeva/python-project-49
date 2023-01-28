from random import randint, choice


def brain_calc():
    correct_answers = 0
    operators = ['+', '*', '-']
    print('Welcome to the Brain Games!')
    name = input('May I have your name?')
    print(f'Hello, {name}')
    print('What is the result of the expression?')
    for i in range(3):
        a = randint(1, 19)
        b = randint(1, 19)
        operator = choice(operators)
        print(f'Question: {a} {operator} {b}')
        p = int(input('Your answer:'))
        if operator == '+':
            if p == a + b:
                print('Correct!')
                correct_answers += 1
            else:
                print(f'\'{p}\' is a wrong answer ;(. Correct answer was \'{a + b}\'.')
                print(f'Let\'s try again, {name}!')
                break
        elif operator == '-':
            if p == a - b:
                print('Correct!')
                correct_answers += 1
            else:
                print(f'\'{p}\' is a wrong answer ;(. Correct answer was \'{a - b}\'.')
                print(f'Let\'s try again, {name}!')
                break
        elif operator == '*':
            if p == a * b:
                print('Correct!')
                correct_answers += 1
            else:
                print(f'\'{p}\' is a wrong answer ;(. Correct answer was \'{a * b}\'.')
                print(f'Let\'s try again, {name}!')
                break
    if correct_answers == 3:
        print(f'Congratulations, {name}!')
