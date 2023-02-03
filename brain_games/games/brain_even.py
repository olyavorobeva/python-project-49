from random import randint


MIN = 1
MAX = 100
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def one_round():
    a = randint(MIN, MAX)
    print(f'Question: {a}')
    p = input('Your answer:')
    answer = 'yes' if a % 2 == 0 else 'no'
    return answer, p
