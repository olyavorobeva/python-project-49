from random import randint
import math
from brain_games.games.greeting import greeting
from brain_games.games.game_logic import logic


MIN = 1
MAX = 100


def one_round():
    a = randint(MIN, MAX)
    b = randint(MIN, MAX)
    print(f'Question: {a} {b}')
    p = int(input('Your answer:'))
    gcd = math.gcd(a, b)
    return gcd, p


def brain_gcd():
    name = greeting()
    print('Find the greatest common divisor of given numbers.')
    logic(one_round, name)
