import prompt
from random import randint
from math import sqrt


def brain_prime():
    correct_answers = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(3):
        is_prime = ''
        digit = randint(1, 100)
        print(f'Question: {digit}')
        p = input('Your answer:')
        prime = True
        j = 2
        while j <= sqrt(digit) and prime is True:
            if digit % j == 0:
                prime = False
            j += 1
        is_prime = 'yes' if prime else 'no'
        if p == is_prime:
            print('Correct!')
            correct_answers += 1
        else:
            print(f'\'{p}\' is a wrong answer ;(. Correct answer was \'{is_prime}\'.')
            break
    if correct_answers == 3:
        print(f'Congratulations, {name}!')