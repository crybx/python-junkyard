import sys


def get_empty_board():
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def print_board(board):
    row_separator = "    -------------------"
    print("      col1  col2  col3  ")
    print(row_separator)

    for i in range(0, 3):
        print(f"row{i + 1}|  {board[i][0]}  |  {board[i][1]}  |  {board[i][2]}  |")
        print(row_separator)


def isWinner(letter, board):
    for i in range(0, 3):
        # check row i
        if board[i][0] == letter and board[i][1] == letter and board[i][2] == letter:
            return True

        # check column i
        if board[0][i] == letter and board[1][i] == letter and board[2][i] == letter:
            return True

    # check both diagonals
    if board[0][0] == letter and board[1][1] == letter and board[2][2] == letter:
        return True

    if board[0][2] == letter and board[1][1] == letter and board[2][0] == letter:
        return True

    return False


def takeTurn(letter, board):
    print(f"your turn {letter}")

    # Check user only enters 1, 2, or 3.
    row = getValidGameInput("which row?: ") - 1
    col = getValidGameInput("which column?: ") - 1

    # Check the space isn't occupied. 
    if board[row][col] == " ":
        board[row][col] = letter
    else:
        print("your chosen spot is occupied. choose somewhere else")
        takeTurn(letter, board)


def getValidGameInput(prompt):
    try:
        # Make sure it's an integer
        choice = input(prompt)
        val = int(choice)

    except ValueError:
        # Typing exit here would be a nice early escape
        if choice == "exit":
            print("bye!")
            sys.exit()
        print("no... input should be 1, 2, or 3")
        return getValidGameInput(prompt)

    if val < 1 or val > 3:
        print("no... input should be 1, 2, or 3")
        return getValidGameInput(prompt)

    return val


def playGame():
    board = get_empty_board()
    print_board(board)
    gameover = False
    turn = 0

    while not gameover:
        takeTurn("x", board)
        turn += 1
        print_board(board)
        if isWinner("x", board):
            print("x wins!")
            gameover = True

        if not gameover and turn >= 9:
            print("tie!")
            gameover = True

        if not gameover:
            takeTurn("o", board)
            turn += 1
            print_board(board)
            if isWinner("o", board):
                print("o wins!")
                gameover = True

        if not gameover and turn >= 9:
            print("tie!")
            gameover = True


play = True

while play:
    playGame()
    restart = input("would you like to play again? y|n: ")
    if restart == "n" or restart == "N" or restart == "no":
        play = False

print("bye!")
