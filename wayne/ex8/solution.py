#!/usr/bin/env python3

# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors 1 beats 3
# Scissors beats paper 3 beats 2
# Paper beats rock 2 beats 1

from enum import Enum, auto

class Move(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

class Again(Enum):
    Yes = True
    No = False
    
def get_winner(player1_move,player2_move):
    print("Player 1 picked %s Player 2 picked %s"%(Move(player1_move).name,Move(player2_move).name))
    #import pdb; pdb.set_trace()
    if player1_move == player2_move:
        print("it's a tie!")
        #Tie
    elif Move(player1_move).name == 'ROCK':
        if Move(player2_move).name == 'PAPER':
            print("Player 2 wins")
        elif Move(player2_move).name == 'SCISSORS':
            print("Player 1 wins")
        else:
            print("Invalid state")
    elif Move(player1_move).name == 'PAPER':
        if Move(player2_move).name == 'ROCK':
            print("Player 2 wins")
        elif Move(player2_move).name == 'SCISSORS':
            print("Player 1 wins")
        else:
            print("Player 2 wins")
    elif Move(player1_move).name == 'SCISSORS':
        if Move(player2_move).name == 'PAPER':
            print("Player 1 wins")
        elif Move(player2_move).name == 'ROCK':
            print("Player 2 wins")
        else: 
            print("Player 2 wins")
    return True

def get_move(player_name):
   for move in Move:
       print("[%s] %s" % (move.value, move.name))
   return int(input("{} Make a move ".format(player_name)))

def play_game():
    player1_move = get_move("Player 1")
    player2_move = get_move("Player 2")
    winner = get_winner(player1_move, player2_move)

def play_again():
   for choice in Again:
       print("[%s] %s" % (int(choice.value), choice.name))
   return int(input("Play again? "))

def main():
   cont = True
   while cont:
       play_game()
       cont = play_again()
   

if __name__ == "__main__":
    main()