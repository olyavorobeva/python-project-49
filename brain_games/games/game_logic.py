def logic(f, name):
    correct_answers = 0
    for i in range(3):
        round, answer, p = f()
        if round:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{p}' is a wrong answer ;(. Correct answer was '{answer}'.")
            print(f'Let\'s try again, {name}!')
            break
    if correct_answers == 3:
        print(f'Congratulations, {name}!')
