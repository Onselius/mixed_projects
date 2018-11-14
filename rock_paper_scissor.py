#! /usr/bin/python3
# rock_paper_scissor.py - A simple rock, paper, scissor game.

import random

def check_winner(player, computer):
    winner = "player"
    choices = {"player": player, "computer": computer}
    frases = {"rock": "Rock breaks scissors", 
            "paper": "Paper covers rock", 
            "scissors": "Scissors cuts paper"}
    if player == computer:
        print("Both choose %s, it's a draw!" % (player))
        return ""
    elif player == "rock":
        if computer == "paper":
            winner = "computer"
    elif player == "paper":
        if computer == "scissors":
            winner = "computer"
    elif player == "scissors":
        if computer == "rock":
            winner = "computer"
    print(frases[choices[winner]])
    return winner

def computer_choice(choices):
    i = random.randint(0, 2)
    return choices[i]

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0
print("Welcome to the rock, paper, scissors game.")
while True:
    print("Pick rock, paper, scissors:")
    player = input().lower()
    if player not in choices:
        print("Not a valid choice, try again!")
        continue

    computer = computer_choice(choices)
    print("Computer chooses %s" % (computer))
    winner = check_winner(player, computer)
    if winner == "player":
        player_score += 1
    elif winner == "computer":
        computer_score += 1

    print("Current score: Player %s | Computer %s" % (player_score, computer_score))
    print("Would you like to play again? Press return to exit")
    again = input().lower()
    if not again:
        break
