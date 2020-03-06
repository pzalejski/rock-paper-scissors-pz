import random
import os

clear = lambda: os.system('cls')

def computer_pick():

    num = random.randint(0,15)

    if num >= 0 and num < 5:
        return 'paper'
    elif num >= 5 and num < 10:
        return 'scissors'
    else:
        return 'rock'


def player_pick():

    ask = input('Choose "rock" , "paper" , "scissors" : ').lower()

    if ask == 'rock':
        return "rock"
    elif ask == 'paper':
        return 'paper'
    elif ask == 'scissors':
        return "scissors"
    else:
        clear()
        print('Invalid selection!')
        return player_pick()

def who_win(player,computer):

    if (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or player == 'scissors' and computer == 'paper':
        return ('Player Wins!')
    elif player == computer:
        return "It's a draw!"
    else:
        return 'Computer Wins!'

def replay():
    new_round = input("Would you like a rematch? Yes or No: ").lower()

    if new_round == 'yes':
        clear()
        return True
    elif new_round =='no':
        clear()
        print('Thank you for playing!')
        return False
    else:
        clear()
        print('Please enter "yes" or "no"')
        return replay()

## Game play below ##

#greeting
print('Welcome to Rock-Paper-Scissors\n')

game_on = True

while game_on:

    #ask the player to pick
    player = player_pick()

    #get the computer's choice
    computer = computer_pick()

    #clear screen
    clear()

    #display player choice and computer choice
    print(f"Player picks: {player}")
    print(f"Computer picks: {computer}")
    print(who_win(player,computer))
    print("\n")


    #checks to see if you would like another round
    if replay() == False:
        game_on = False

    

