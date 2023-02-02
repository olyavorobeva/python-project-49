from random import randint


MIN_STEP = 1
MAX_STEP = 3
MIN_PROGRESSION = 1
MAX_PROGRESSION = 100
RULES = 'What number is missing in the progression?'


def one_round():
    length_of_ls = 10
    step = randint(MIN_STEP, MAX_STEP)
    progression = randint(1, 100)
    ls = []
    for i in range(progression, progression + (length_of_ls * step), step):
        ls.append(i)
    index_of_the_missing_number = randint(0, len(ls) - 1)
    missing_number = ls[index_of_the_missing_number]
    ls[index_of_the_missing_number] = '..'
    print(f'Question: {" ".join([str(x) for x in ls])}')
    p = int(input('Your answer:'))
    return missing_number, p
