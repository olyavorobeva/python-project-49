from random import randint
import math


MIN = 1
MAX = 100
RULES = 'Find the greatest common divisor of given numbers.'


def execute_one_round():
    start = randint(MIN, MAX)
    finish = randint(MIN, MAX)
    print(f'Question: {start} {finish}')
    response = int(input('Your answer:'))
    gcd = math.gcd(start, finish)
    return gcd, response
