import hangman
import sys
import tic_tac_toe


def print_available_games():
    print()
    print("1: Hangman")
    print("2: Tic-Tac-Toe")
    print()


def pick_a_game():
    choice = input("Enter the number of the game to play. Type 'exit' to quit: ")
    err_msg = "That's not a valid game choice"

    if choice == "exit":
        print("Goodbye ~")
        sys.exit()

    try:
        game_number = int(choice)
        if 0 < game_number < 3:
            return game_number
        else:
            print(err_msg)
            return pick_a_game()
    except ValueError:
        print(err_msg)
        return pick_a_game()


def main():
    while True:
        print_available_games()
        print("Would you like to play a game?")
        choice = pick_a_game()
        if choice == 1:
            hangman.play_game()
        elif choice == 2:
            tic_tac_toe.play_game()
        else:
            print("Sorry, that game doesn't work yet.")


if __name__ == "__main__":
    main()
