import random


def print_board(board):
    print()
    print("-------------")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("-------------    key:")
    print(f"| {board[3]} | {board[4]} | {board[5]} |    |1|2|3|")
    print("-------------    |4|5|6|")
    print(f"| {board[6]} | {board[7]} | {board[8]} |    |7|8|9|")
    print("-------------")
    print()


def take_turn(board, player):
    print_board(board)
    print(f"Your turn {player}")
    spot = get_valid_spot("Which spot?: ")

    if board[spot] == "_":
        board[spot] = player
    else:
        print("Your chosen spot is occupied, please choose another")
        return take_turn(board, player)


def take_computer_turn(board, player):
    empty_spots = [i for i, p in enumerate(board) if p == "_"]
    spot = random.choice(empty_spots)
    board[spot] = player


def get_valid_spot(prompt):
    err_msg = "Input should be a number from 1 to 9"

    try:
        # make sure input is an integer
        choice = input(prompt)
        val = int(choice)

        # make sure the integer is in the proper range
        if 0 < val < 10:
            # adjust to zero-based
            return val - 1

        print(err_msg)
        return get_valid_spot(prompt)

    except ValueError:
        print(err_msg)
        return get_valid_spot(prompt)


def check_for_win(board, p):
    winning_combos = ("012", "345", "678", "036", "147", "258", "048", "246")

    for combo in winning_combos:
        spots = [int(num) for num in combo]

        if board[spots[0]] == p and board[spots[1]] == p and board[spots[2]] == p:
            print_board(board)
            print(f"{p} wins!")
            return True

    # check for tie
    if "_" not in board:
        print_board(board)
        print("It's a tie!")
        return True

    return False


def get_number_of_players():
    try:
        choice = input("How many players? (1 or 2): ")
        return int(choice)
    except ValueError:
        print("Input must be the number 1 or 2")
        return get_number_of_players()


def play_game():
    print("---------------")
    print("- TIC-TAC-TOE -")
    print("---------------")
    board = list("_" * 9)
    game_over = False
    player1 = "X"
    player2 = "O"
    players = get_number_of_players()

    while not game_over:
        # X take turn
        take_turn(board, player1)
        game_over = check_for_win(board, player1)

        if not game_over:
            # O take turn
            if players == 1:
                take_computer_turn(board, player2)
            elif players == 2:
                take_turn(board, player2)
            game_over = check_for_win(board, player2)

    again = input("Game over. Would you like to play again? y|n: ")

    if again.lower() in ("y", "yes", "sure"):
        play_game()


if __name__ == "__main__":
    play_game()
    print("Goodbye ~")
