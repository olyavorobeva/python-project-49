from random import randint
import prompt


def brain_progression():
    correct_answers = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    for i in range(3):
        length_of_ls = 10
        step = randint(1, 3)
        start = randint(1, 100)
        ls = []
        for i in range(start, start+(length_of_ls*step), step):
            ls.append(i)
        index_of_the_missing_number = randint(0, len(ls)-1)
        missing_number = ls[index_of_the_missing_number]
        ls[index_of_the_missing_number] = '..'
        print(f'Question: {" ".join([str(x) for x in ls])}')
        p = int(input('Your answer:'))
        if p == missing_number:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{p}' is wrong answer ;(. Correct answer was '{missing_number}'.")
            print(f'Let\'s try again, {name}!')
            break
    if correct_answers == 3:
        print(f'Congratulations, {name}!')