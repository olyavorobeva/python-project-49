from random import randint
import math
from brain_games.games.greeting import greeting
from brain_games.games.game_logic import logic


def one_round():
    a = randint(1, 100)
    b = randint(1, 100)
    print(f'Question: {a} {b}')
    p = int(input('Your answer:'))
    gcd = math.gcd(a, b)
    return gcd, p


def brain_gcd():
    name = greeting()
    print('Find the greatest common divisor of given numbers.')
    logic(one_round, name)
