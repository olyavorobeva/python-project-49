from random import randint
from brain_games.games.greeting import greeting
from brain_games.games.game_logic import logic


def one_round():
    length_of_ls = 10
    step = randint(1, 3)
    start = randint(1, 100)
    ls = []
    for i in range(start, start + (length_of_ls * step), step):
        ls.append(i)
    index_of_the_missing_number = randint(0, len(ls) - 1)
    missing_number = ls[index_of_the_missing_number]
    ls[index_of_the_missing_number] = '..'
    print(f'Question: {" ".join([str(x) for x in ls])}')
    p = int(input('Your answer:'))
    return missing_number, p


def brain_progression():
    name = greeting()
    print('What number is missing in the progression?')
    logic(one_round, name)
