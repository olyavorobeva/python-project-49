from random import randint, choice


MIN = 1
MAX = 19
RULES = 'What is the result of the expression?'


def calculate(first_number, second_number, operator):
    if operator == '+':
        return first_number + second_number
    elif operator == '-':
        return first_number - second_number
    elif operator == '*':
        return first_number * second_number


def execute_one_round():
    operators = ['+', '*', '-']
    first_number = randint(MIN, MAX)
    second_number = randint(MIN, MAX)
    operator = choice(operators)
    question = f'{first_number} {operator} {second_number}'
    answer = calculate(first_number, second_number, operator)
    return str(answer), question
