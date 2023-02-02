from random import randint
import math


MIN = 1
MAX = 100
RULES = 'Find the greatest common divisor of given numbers.'


def one_round():
    a = randint(MIN, MAX)
    b = randint(MIN, MAX)
    print(f'Question: {a} {b}')
    p = int(input('Your answer:'))
    gcd = math.gcd(a, b)
    return gcd, p
