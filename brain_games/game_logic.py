from brain_games.games.greeting import greeting


def execute_main_logic(module):
    name = greeting()
    correct_answers = 0
    print(module.RULES)
    ROUNDS = 3
    for _ in range(ROUNDS):
        answer, response = module.execute_one_round()
        if answer == response:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{response}' is a wrong answer ;(. Correct answer was '{answer}'.")
            print(f'Let\'s try again, {name}!')
            break
    if correct_answers == ROUNDS:
        print(f'Congratulations, {name}!')
