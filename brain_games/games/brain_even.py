from random import randint


def even_game():
    correct_answers = 0
    print('Welcome to the Brain Games!')
    name = input('May I have your name?')
    print('Answer "yes" if number is even, otherwise answer "no".')
    for i in range(3):
        a = randint(1, 100)
        print(f'Question: {a}')
        p = input('Your answer:')
        if (p == 'yes' and a % 2 == 0) or (p == 'no' and a % 2 == 1):
            print('Correct!')
            correct_answers += 1
        else:
            g = a % 2
            if g == 0:
                g = 'yes'
            else:
                g = 'no'
            print(f'\'{p}\' is a wrong answer ;(. Correct answer was \'{g}\'.')
            print(f'Let\'s try again, {name}!')
            break
    if correct_answers == 3:
        print(f'Congratulations, {name}!')
