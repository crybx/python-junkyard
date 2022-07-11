
def create_board():
    return [list("___"), list("___"), list("___")]


def print_board(board):
    for row in range(0, 3):
        print(f"| {board[row][0]} | {board[row][1]} | {board[row][2]} |")


def check_for_win(board, p, turn_num):
    for i in range(0, 3):
        # check rows, i is row
        if board[i][0] == p and board[i][1] == p and board[i][2] == p:
            print(f"{p} wins in row {i}!")
            return True

        # check columns, i is column
        if board[0][i] == p and board[1][i] == p and board[2][i] == p:
            print(f"{p} wins in column {i}!")
            return True

    # check diagonals
    if board[0][0] == p and board[1][1] == p and board[2][2] == p:
        print(f"{p} wins by diagonal!")
        return True

    if board[0][2] == p and board[1][1] == p and board[2][0] == p:
        print(f"{p} wins by diagonal!")
        return True

    # check if tie
    if turn_num >= 9:
        print("IT'S A TIE!")
        return True

    return False


def take_turn(letter, board):
    print_board(board)
    print(f"your turn {letter}")

    row = get_valid_input("which row?: ")
    col = get_valid_input("which column?: ")

    if board[row][col] == "_":
        board[row][col] = letter
    else:
        print("your chosen spot is occupied, please choose another")
        return take_turn(letter, board)


def get_valid_input(prompt):
    # get input for a move
    try:
        # make sure input is an integer
        choice = input(prompt)
        val = int(choice)

    except ValueError:
        print("no...input should be 0, 1, or 2")
        return get_valid_input(prompt)

    # make sure the integer is in the proper range
    if val < 0 or val > 2:
        print("no...input should be 0, 1, or 2")
        return get_valid_input(prompt)

    return val


def play_game():
    board = create_board()
    gameover = False
    turn_num = 0

    while not gameover:
        take_turn("x", board)
        turn_num += 1
        gameover = check_for_win(board, "x", turn_num)

        if not gameover:
            take_turn("o", board)
            turn_num += 1
            gameover = check_for_win(board, "o", turn_num)

    print_board(board)


play_game()
print("THE END")
