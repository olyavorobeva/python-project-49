from random import randint
from math import sqrt
from brain_games.games.greeting import greeting
from brain_games.games.game_logic import logic


def check_prime(a):
    prime = True
    j = 2
    while j <= sqrt(a) and prime is True:
        if a % j == 0:
            prime = False
        j += 1
    return prime


def one_round():
    digit = randint(1, 100)
    print(f'Question: {digit}')
    p = input('Your answer:')
    is_prime = 'yes' if check_prime(digit) else 'no'
    if p == is_prime:
        return True, is_prime, p
    else:
        return False, is_prime, p


def brain_prime():
    name = greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    logic(one_round, name)
