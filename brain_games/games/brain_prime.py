from random import randint
from math import sqrt


MIN = 1
MAX = 100
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_prime(a):
    prime = True
    j = 2
    while j <= sqrt(a) and prime is True:
        if a % j == 0:
            prime = False
        j += 1
    return prime


def execute_one_round():
    digit = randint(MIN, MAX)
    question = f'{digit}'
    is_prime = 'yes' if check_prime(digit) else 'no'
    return is_prime, question
