def print_board(b):
    print("---------")
    print("| " + b[0] + " " + b[1] + " " + b[2] + " |")
    print("| " + b[3] + " " + b[4] + " " + b[5] + " |")
    print("| " + b[6] + " " + b[7] + " " + b[8] + " |")
    print("---------")


def check_game_state(board):
    if abs(board.count("X") - board.count("O")) > 1:
        print("Impossible")
        return True

    winning_combos = ['012', '345', '678', '036', '147', '258', '048', '246']
    x_wins = False
    o_wins = False

    for combination in winning_combos:
        spots = [int(num) for num in combination]

        if board[spots[0]] == board[spots[1]] == board[spots[2]]:
            if board[spots[0]] == "_":
                continue
            elif board[spots[0]] == "X":
                x_wins = True
            elif board[spots[0]] == "O":
                o_wins = True

    if x_wins and o_wins:
        print("Impossible")
        return True
    elif x_wins:
        print("X wins")
        return True
    elif o_wins:
        print("O wins")
        return True
    elif "_" not in board:
        print("Draw")
        return True
    else:
        # print("Game not finished")
        return False


def update_spot_on_board(board, row, col, letter):
    i = col + 2
    j = row - 1
    index = (j * 3 + i) - 3

    if board[index] != "_":
        print("This cell is occupied! Choose another one!")
        do_move(board, letter)
    else:
        board[index] = letter


def do_move(board, letter):
    try:
        choice = input("Enter the coordinates: ")
        row, col = choice.split()
        row = int(row)
        col = int(col)
        if row > 3 or row < 1 or col > 3 or col < 1:
            print("Coordinates should be from 1 to 3!")
            do_move(board, letter)
        else:
            update_spot_on_board(board, row, col, letter)

    except ValueError:
        print("You should enter numbers!")
        do_move(board, letter)


def play_game():
    board = list("_" * 9)
    game_over = False
    print_board(board)

    while not game_over:
        do_move(board, "X")
        print_board(board)
        game_over = check_game_state(board)

        if not game_over:
            do_move(board, "O")
            print_board(board)
            game_over = check_game_state(board)


play_game()
