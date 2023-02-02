def logic(f, name):
    correct_answers = 0
    ROUNDS = 3
    for _ in range(ROUNDS):
        answer, p = f()
        if answer == p:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{p}' is a wrong answer ;(. Correct answer was '{answer}'.")
            print(f'Let\'s try again, {name}!')
            break
    if correct_answers == ROUNDS:
        print(f'Congratulations, {name}!')
