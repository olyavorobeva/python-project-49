from random import randint
import prompt, math

def brain_gcd():
    correct_answers = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    for i in range(3):
        a = randint(1, 100)
        b = randint(1, 100)
        print(f'Question: {a} {b}')
        p = int(input('Your answer:'))
        gcd = math.gcd(a, b)
        if p == gcd:
            print('Correct!')
            correct_answers += 1
        else:
            print(f'\'{p}\' is wrong answer ;(. Correct answer was \'{gcd}\'.')
            print(f'Let\'s try again {name}!')
            break
    if correct_answers == 3:
        print(f'Congratulations, {name}!')


