from random import randint


MIN_STEP = 1
MAX_STEP = 3
MIN_PROGRESSION = 1
MAX_PROGRESSION = 100
RULES = 'What number is missing in the progression?'
LENGTH = 10


def make_progression():
    step = randint(MIN_STEP, MAX_STEP)
    progression = randint(MIN_PROGRESSION, MAX_PROGRESSION)
    ls = []
    for i in range(progression, progression + (LENGTH * step), step):
        ls.append(i)
    return ls


def delete_random_number_in_progression(ls):
    index_of_the_missing_number = randint(0, len(ls) - 1)
    missing_number = ls[index_of_the_missing_number]
    ls[index_of_the_missing_number] = '..'
    return missing_number


def execute_one_round():
    ls = make_progression()
    missing_number = delete_random_number_in_progression(ls)
    question = " ".join([str(x) for x in ls])
    return str(missing_number), question
