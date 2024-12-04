"""
Author: Joe George
Date: 3 December 2024
Play Monty Hall game
"""


# THIS CODE DOESN'T WORK AS INTENDED OF NOW

import random

def montyhall():
    print("Welcome to the Monty Hall Game!")
    doors = {
        1:"Goat",
        2:"Car",
        3:"Goat"
    }

    player_choice = int(input("Choose a door (1, 2, or 3): "))

    if player_choice in doors:
        print(f"The door you opened Door-{player_choice} had a {doors.get(player_choice)} in it.")
        switch_choice = input("Do you want to switch? (y/n)")
        if switch_choice == "y" or "Y":
            new_player_choice = int(input(f"Which other choice do you want: "))
            if new_player_choice == 2:
                print(f"The door you opened {player_choice} had a {doors.get(player_choice)} in it. \n CONGRATS!!! YOU WIN🎉🎉🎉🎉🎉")
            elif new_player_choice in doors and player_choice == 1 or 3:
                print(f"The door you opened {player_choice} had a {doors.get(player_choice)} in it. \n SORRY!!! YOU LOST...")
montyhall()
















