from random import randint
from brain_games.games.greeting import greeting
from brain_games.games.game_logic import logic


def one_round():
    a = randint(1, 100)
    print(f'Question: {a}')
    p = input('Your answer:')
    answer = 'yes' if p % 2 == 0 else 'no'
    if p == answer:
        return True, answer, p
    else:
        return False, answer, p


def even_game():
    name = greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    logic(one_round, name)
