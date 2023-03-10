def greeting():
    print('Welcome to the Brain Games!')
    name = input('May I have your name?')
    print(f'Hello, {name}!')
    return name


def execute_main_logic(module):
    name = greeting()
    correct_answers = 0
    print(module.RULES)
    ROUNDS = 3
    for _ in range(ROUNDS):
        answer, question = module.execute_one_round()
        print(f'Question: {question}')
        response = input('Your answer:')
        if answer == response:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{response}' is a wrong answer ;(.", end='')
            print(f"Correct answer was '{answer}'.")
            print(f'Let\'s try again, {name}!')
            break
    if correct_answers == ROUNDS:
        print(f'Congratulations, {name}!')
