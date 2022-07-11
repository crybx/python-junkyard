import sys


def create_board():
    return list("_" * 9)


def print_board(board):
    print(f"|0 {board[0]} |1 {board[1]} |2 {board[2]} |")
    print(f"|3 {board[3]} |4 {board[4]} |5 {board[5]} |")
    print(f"|6 {board[6]} |7 {board[7]} |8 {board[8]} |")


def check_for_win(board, player):
    winning_combos = ('012', '345', '678', '036', '147', '258', '048', '246')

    for combination in winning_combos:
        spots = [int(num) for num in combination]

        if (board[spots[0]] == player
                and board[spots[1]] == player
                and board[spots[2]] == player):
            print_board(board)
            print(f"{player} wins!")
            return True

    # check for a tie
    if "_" not in board:
        print_board(board)
        print("IT'S A TIE!")
        return True

    return False


def take_turn(board, letter):
    print_board(board)
    print(f"your turn {letter}")

    spot = get_valid_input("which spot?: ")

    if board[spot] == "_":
        board[spot] = letter
    else:
        print("your chosen spot is occupied, please choose another")
        return take_turn(board, letter)


def get_valid_input(prompt):
    # get input for a move
    choice = ""
    try:
        # make sure input is an integer
        choice = input(prompt)
        val = int(choice)

        # make sure the integer is in the proper range
        if val < 0 or val > 8:
            print("no...input should be number from 0 to 8")
            return get_valid_input(prompt)

        return val

    except ValueError:
        if choice == "exit":
            print("farewell friend ~")
            sys.exit()
        print("no...input should be number from 0 to 8")
        return get_valid_input(prompt)


def play_game():
    board = create_board()
    player1 = "x"
    player2 = "o"
    game_over = False

    while not game_over:
        take_turn(board, player1)
        game_over = check_for_win(board, player1)

        if not game_over:
            take_turn(board, player2)
            game_over = check_for_win(board, player2)


if __name__ == "__main__":
    play_game()
    print("THE END")
