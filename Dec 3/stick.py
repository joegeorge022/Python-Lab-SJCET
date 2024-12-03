"""
Author: Joe George
Date: 3 December 2024
Play Stick game
"""

def stick_game():
    print("Welcome to the Stick Game!")
    total_sticks = 16
    player1 = input("Player-1, enter your name: ")
    player2 = input("Player-2, enter your name: ")

    while total_sticks > 0:
        # PLAYER 1 PART
        p1_turn = int(input(f"{player1}! How many sticks you want to take(1,2 or 3): "))
        if p1_turn not in [1,2,3]:
            print("Invalid Number of Sticks. You miss your turn as punishment")
        else:
            total_sticks -= p1_turn
            print(f"{player1} takes {p1_turn} stick(s). Remaining sticks: {total_sticks}")

        if total_sticks <= 0:
            print(f"{player1} loses!")
            break

        # PLAYER 2 PART
        p2_turn = int(input(f"{player2}! How many sticks you want to take(1,2 or 3): "))
        if p2_turn not in [1,2,3]:
            print("Invalid Number of Sticks. You miss your turn as punishment")
        else:
            total_sticks -= p2_turn
            print(f"{player2} takes {p2_turn} stick(s). Remaining sticks: {total_sticks}")

        if total_sticks <= 0:
            print(f"{player2} loses!")
            break

stick_game()

















