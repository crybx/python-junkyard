import hangman
import sys
import tic_tac_toe
import tower_of_hanoi
from alien_mystery_island_game import alien_mystery_island

# Create a dictionary of games
games = {
    1: [hangman, "Hangman"],
    2: [tic_tac_toe, "Tic Tac Toe"],
    3: [tower_of_hanoi, "Tower of Hanoi"],
    4: [alien_mystery_island, "Alien Mystery Island"],
}


def print_available_games():
    for game in games:
        print(f"  {game}: {games[game][1]}")


def pick_a_game():
    print("Pick a game by typing the number next to it.")
    print("Type 'exit' to quit.")
    choice = input("> ")
    err_msg = "That's not a valid game choice"

    if choice.lower() == "exit":
        print("Goodbye ~")
        sys.exit()

    try:
        game_number = int(choice)
        # Make sure the game number is valid
        if game_number not in games:
            print(err_msg)
            return pick_a_game()
        return game_number
    except ValueError:
        print(err_msg)
        return pick_a_game()


def main():
    while True:
        print("Would you like to play a game?")
        print_available_games()
        choice = pick_a_game()
        games[choice][0].play_game()


main()
