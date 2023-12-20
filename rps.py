import random
choices=['rock','paper','scissors']
play_string='Your choice was {} '
computer_string='The computers choice was {} '
while True:
    player_chioce= input("pick a choice rock,paper,scissors  ").lower()
    computer_choice = random.choice(choices)
    if player_chioce not in choices:
        print('enter a valid input')
        continue
    if player_chioce.lower() in ['exit', 'quit']:
       break
    if player_chioce==computer_choice:
        print(play_string.format(player_chioce) )
        print(computer_string.format(computer_choice))
        print('TIE')
    elif player_chioce== 'rock' and computer_choice=='scissors' :
        print(play_string.format(player_chioce))
        print(computer_string.format(computer_choice))
        print('you win')
    elif player_chioce== 'rock' and computer_choice=='paper' :
        print(play_string.format(player_chioce))
        print(computer_string.format(computer_choice))
        print('You lose')
    elif player_chioce== 'scissors' and computer_choice=='rock' :
        print(play_string.format(player_chioce))
        print(computer_string.format(computer_choice))
        print('You lose')
    elif player_chioce== 'scissors' and computer_choice=='paper' :
        print(play_string.format(player_chioce))
        print(computer_string.format(computer_choice))
        print('You WIN')
    elif player_chioce== 'paper' and computer_choice=='scissors' :
        print(play_string.format(player_chioce))
        print(computer_string.format(computer_choice))
        print('You lose')
    elif player_chioce== 'paper' and computer_choice=='rock' :
        print(play_string.format(player_chioce))
        print(computer_string.format(computer_choice))
        print('You Win')
        
print('THANK YOU FOR THE GAME')    

