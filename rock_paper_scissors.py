import random

moves = ['rock', 'paper', 'scissors']
player_wins = ['paper rock', 'scissors paper', 'rock scissors']

while True:
    player_move = input("Your Move: ")
    if player_move == 'quit':
        break
    if player_move not in moves:
        print("Allowed Moves: ", moves)
        break
    computer_move = random.choice(moves)

    print("You: ", player_move)
    print("Me: ", computer_move)
    abc = player_move + " " + computer_move
    if player_move == computer_move:
        print("Tie")
    elif abc in player_wins:
        print("You Win!")
    else:
        print("You Lose!")
