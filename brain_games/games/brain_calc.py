from random import randint, choice
from brain_games.games.greeting import greeting
from brain_games.games.game_logic import logic


def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b


def one_round():
    operators = ['+', '*', '-']
    a = randint(1, 19)
    b = randint(1, 19)
    operator = choice(operators)
    print(f'Question: {a} {operator} {b}')
    p = int(input('Your answer:'))
    answer = calculate(a, b, operator)
    return answer, p


def brain_calc():
    name = greeting()
    print('What is the result of the expression?')
    logic(one_round, name)
