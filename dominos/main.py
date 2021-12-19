from os import system
import sys
import re
from multiprocessing.pool import ThreadPool
from CloudSave import CloudSave
from GameBoard import GameBoard
from PllayerHand import PlayerHand


def validate_input(message, regex, error_msg=None):
    regex = re.compile(regex)
    user_input = input(message)
    match = regex.match(user_input)

    while not match:
        if error_msg:
            print(error_msg)
        user_input = input(message)
        match = regex.match(user_input)

    return user_input


if __name__ == "__main__":
    # Create CloudSave object in the background
    save = ThreadPool().apply_async(CloudSave, ("Dominos Stats", "credentials.json"))

    print("Welcome to Dominos!\n")

    while True:
        print("A) Read the rules")
        print("B) View the scoreboard")
        print("C) Start a new game")
        print("Press any other button to quit\n")
        choice = input("Select an option: ")
        print()

        if choice.lower() == "a":
            print("Each player will start with 7 dominos. The player with the highest double starts. In the case that no player has a double, the player with the domino that has the highest sum will start. Players will then take turns placing a domino in the center of the board. To place a domino, one of the sides must have a matching number to the center domino in play. If the player doesn't have a domino that meets this requirement, then they must draw another domino from the deck. Play continues until one of the players runs out of dominos.\n")
            input("Press enter to continue\n")

        elif choice.lower() == "b":
            save.get().display_scoreboard()
            input("Press enter to continue\n")

        elif choice.lower() == "c":
            validate_input("How many players: ", "^2$", "Must be 2!")

            player1 = validate_input("Enter Player 1 name: ",
                                     "^[a-zA-Z ]+$", "Must only contain characters and spaces!")

            player2 = validate_input("Enter Player 2 name: ",
                                     "^[a-zA-Z ]+$", "Must only contain characters and spaces!")

            validate_input("How many games: ",
                           "^\d*[13579]$", "Must be an odd number! ")

            print()
            print("Setting up the game board...")
            board = GameBoard()
            print("Dealing hands...")

            # Give 7 dominos to each player
            player1hand = PlayerHand(board.deal_hand(7))
            player2hand = PlayerHand(board.deal_hand(7))
            current_hand = []

            domino1 = player1hand.get_highest_domino()
            domino2 = player2hand.get_highest_domino()
            compare_hands = PlayerHand([domino1, domino2])

            if compare_hands.get_highest_domino() == domino1:
                current_player = 1
                current_player_name = player1
                current_hand = player1hand
                other_hand = player2hand

            else:
                current_player = 2
                current_player_name = player2
                current_hand = player2hand
                other_hand = player1hand

            print(
                f"{current_player_name} gets to go first because they have the highest domino")
            print(
                f"Please pass the screen to {current_player_name}, then press enter")
            input()

            while current_hand.size() > 0:
                print()
                print(f"{current_player_name}'s turn: ")
                print(f"Current domino on the board: {board.domino}")
                print(f"Your hand: {current_hand}")
                print(f"Other player has {other_hand.size()} dominos left")
                domino = input(
                    "Enter the domino you would like to play or 'DRAW': ")

                if domino.upper() == "DRAW":
                    current_hand.add_domino(board.draw_domino())

                elif domino in current_hand:
                    if board.place_domino(domino):
                        current_hand.remove_domino(domino)
                        if current_hand.size() <= 0:
                            print(
                                f"Congratulations! {current_player_name} won the game!")
                            print(
                                f"The other player still had {other_hand.size()} dominos left")

                            save.get().add_win(current_player)
                            print("The score has been updated")

                        elif current_player == 1:
                            player1hand = current_hand
                            print(
                                f"Please pass the screen to {player2}, then press enter")
                            input()
                            current_player = 2
                            current_player_name = player2
                            current_hand = player2hand
                            other_hand = player1hand

                        elif current_player == 2:
                            player2hand = current_hand
                            print(
                                f"Please pass the screen to {player1}, then press enter")
                            input()
                            current_player = 1
                            current_player_name = player1
                            current_hand = player1hand
                            other_hand = player2hand
                    else:
                        print("You can't place that domino on the board!")

                else:
                    print("You don't have that domino in your hand!")
        else:
            sys.exit(0)
