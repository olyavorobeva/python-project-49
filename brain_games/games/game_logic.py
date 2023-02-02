from brain_games.games.greeting import greeting



def logic(module):
    name = greeting()
    correct_answers = 0
    print(module.RULES)
    ROUNDS = 3
    for _ in range(ROUNDS):
        answer, p = module.one_round()
        if answer == p:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{p}' is a wrong answer ;(. Correct answer was '{answer}'.")
            print(f'Let\'s try again, {name}!')
            break
    if correct_answers == ROUNDS:
        print(f'Congratulations, {name}!')
