import hangman
import sys
import tic_tac_toe
import tower_of_hanoi


# Create a dictionary of games
games = {
    1: hangman,
    2: tic_tac_toe,
    3: tower_of_hanoi
}


def print_available_games():
    for game in games:
        print(f"  {game}: {games[game].__name__}")


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
        games[choice].play_game()


if __name__ == "__main__":
    main()
