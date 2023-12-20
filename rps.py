import random
choices=['rock','paper','scissors']
while True:
    player_chioce= input("pick a choice rock,paper,scissors  ").lower()
    computer_choice = random.choice(choices)
    if player_chioce not in choices:
        print('enter a valid input')
        continue
    if player_chioce.lower() in ['exit', 'quit']:
       break
    if player_chioce==computer_choice:
        print(f'your choice was {player_chioce}' )
        print(f'The computers choice was {computer_choice}')
        print('TIE')
    elif player_chioce== 'rock' and computer_choice=='scissors' :
        print(f'your choice was {player_chioce}' )
        print(f'The computers choice was {computer_choice}')
        print('you win')
    elif player_chioce== 'rock' and computer_choice=='paper' :
        prin(f'your choice was {player_chioce}' )
        print(f'The computers choice was {computer_choice}')
        print('You lose')
    elif player_chioce== 'scissors' and computer_choice=='rock' :
        print(f'your choice was{ player_chioce}' )
        print(f'The computers choice was {computer_choice}')
        print('You lose')
    elif player_chioce== 'scissors' and computer_choice=='paper' :
        print(f'your choice was {player_chioce}' )
        print(f'The computers choice was {computer_choice}')
        print('You WIN')
    elif player_chioce== 'paper' and computer_choice=='scissors' :
        print(f'your choice was {player_chioce}' )
        print(f'The computers choice was {computer_choice}')
        print('You lose')
    elif player_chioce== 'paper' and computer_choice=='rock' :
        print(f'your choice was {player_chioce}' )
        print(f'The computers choice was {computer_choice}')
        print('You Win')
            
print('THANK YOU FOR THE GAME')    

