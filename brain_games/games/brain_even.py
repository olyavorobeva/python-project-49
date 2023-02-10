from random import randint


MIN = 1
MAX = 100
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def execute_one_round():
    number = randint(MIN, MAX)
    question = f'{number}'
    answer = 'yes' if number % 2 == 0 else 'no'
    return answer, question
