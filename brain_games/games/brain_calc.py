from random import randint, choice


MIN = 1
MAX = 19
RULES = 'What is the result of the expression?'


def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b


def one_round():
    operators = ['+', '*', '-']
    a = randint(MIN, MAX)
    b = randint(MIN, MAX)
    operator = choice(operators)
    print(f'Question: {a} {operator} {b}')
    p = int(input('Your answer:'))
    answer = calculate(a, b, operator)
    return answer, p
