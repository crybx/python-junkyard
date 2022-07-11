def print_board(board):
    div_line = "-------------"
    print()
    print(div_line)
    for i in range(0, 3):
        print(f"| {board[i][0]} | {board[i][1]} | {board[i][2]} |")
        print(div_line)
    print()


def take_turn(board, player):
    print_board(board)
    print(f"your turn {player}")
    row, col = get_valid_input()

    if board[row][col] == "_":
        board[row][col] = player
    else:
        print("your chosen spot is occupied, please choose another")
        return take_turn(board, player)


def get_valid_input():
    err_msg = "row and column must be number from 1 to 3 with a comma between"

    try:
        choice = input("enter the row and column (example: 1,3): ")
        row, col = choice.split(",")
        row, col = int(row), int(col)
        if 0 < row < 4 and 0 < col < 4:
            return row - 1, col - 1
        else:
            print(err_msg)
            return get_valid_input()
    except ValueError:
        print(err_msg)
        return get_valid_input()


def check_for_win(board, p):
    win_msg = f"\n{p} wins!"
    is_spot_open = False

    for i in range(0, 3):
        # check rows
        if board[i][0] == p and board[i][1] == p and board[i][2] == p:
            print(win_msg)
            return True

        # check columns
        if board[0][i] == p and board[1][i] == p and board[2][i] == p:
            print(win_msg)
            return True

        # check for open spots in each row
        if "_" in board[i]:
            is_spot_open = True

    if not is_spot_open:
        print("It's a tie!")
        return True

    # check diagonals
    if board[0][0] == p and board[1][1] == p and board[2][2] == p:
        print(win_msg)
        return True

    if board[0][2] == p and board[1][1] == p and board[2][0] == p:
        print(win_msg)
        return True

    return False


def play_game():
    board = [list("___"), list("___"), list("___")]
    player1 = "X"
    player2 = "O"
    game_over = False

    while not game_over:
        take_turn(board, player1)
        game_over = check_for_win(board, player1)

        if not game_over:
            take_turn(board, player2)
            game_over = check_for_win(board, player2)

    print_board(board)
    print("Game Over")


if __name__ == "__main__":
    play_game()
    print("bye friend")
