def new_game():
    guesses = []
    correct_guesses = 0
    var = 0
    for key in questions:
        print(key)
        for val in options[var]:
            print(val)
        var += 1
        guess = input('ANSWER {\'A\',\'B\',\'C\',\'D\'}: ').upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
    display_score(correct_guesses, guesses)
    play_again()


def check_answer(answer, guess):

    if answer == guess:
        print('CORRECT')
        return 1
    else:
        return 0


def display_score(correct_guesses, guesses):
    print('-------------------------------------------')
    print('----RESULTS----')
    print('ANSWERS', end='\n')
    for value in questions.values():
        print(value, end='\n')
    print('-------------------------------------------')
    print('Guesses', end='\n')
    for value in guesses:
        print(value, end='\n')
    score = int((correct_guesses/len(questions)) * 100)
    print(f'YOUR SCORE WAS {score}'+'%')


def play_again():
    play = input('DO YOU WANT TO PLAY AGAIN Y/N ')
    if play.lower() == 'y':
        return True
    else:
        return False


questions = {'Who discovered the  Gravitational Constant': 'A',
             'Who discovered the most beautiful equation in Mathematics': 'D',
             'Who is the present President of Nigeria':  'C',
             'Who is credited for discovering the particle nature of light': 'B'
             }
options = [['A.Isaac Newton', 'B.Benjamin Franklin', 'Albert E', 'D.Max Plank'],
           ['A.Gauss', 'B.Avogadro', 'C.Bohr', 'D.Euler'],
           ['A.Buhari', 'B.Skonekan', 'C.Abacha', 'D.BAT'],
           ['A.Miguel', 'B.Albert E', 'C.John Fourier', 'D.Lebesgue']
           ]
new_game()
while play_again():
    new_game()
