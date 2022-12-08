import sys


def create_towers():
    return [[3, 2, 1], [], []]


def get_tower_piece(value: int) -> str:
    if value == 1:
        return "   [=|=]   "
    elif value == 2:
        return "  [==|==]  "
    elif value == 3:
        return " [===|===] "
    else:
        return "     |     "


def draw_towers(towers):
    rows = ["", "", ""]
    for x in range(3):
        tower = towers[x]
        for y in range(3):
            if y < len(tower):
                rows[y] += get_tower_piece(tower[y])
            else:
                rows[y] += get_tower_piece(0)

    # print the rows in reverse order
    for row in rows[::-1]:
        print(row)

    print(" ----1----  ----2----  ----3---- ")


def get_valid_input(prompt):
    try:
        # Make sure it's an integer
        choice = input(prompt)
        val = int(choice)

    except ValueError:
        # Typing exit here would be a nice early escape
        if choice == "exit":
            print("Bye!")
            sys.exit()
        print("No... input should be 1, 2, or 3")
        return get_valid_input(prompt)

    if val < 1 or val > 3:
        print("No... input should be 1, 2, or 3")
        return get_valid_input(prompt)

    return val


def play_game():
    print("Welcome to the Tower of Hanoi!")
    towers = create_towers()
    moves = 0

    while True:
        draw_towers(towers)
        from_tower = get_valid_input("Which tower do you want to move from?: ")
        from_tower -= 1
        to_tower = get_valid_input("Which tower do you want to move to?: ")
        to_tower -= 1
        # check if the move is valid by
        # checking if the from_tower has a piece
        # and if the to_tower is empty or if the piece is smaller
        if towers[from_tower] and (not towers[to_tower] or towers[from_tower][-1] < towers[to_tower][-1]):
            towers[to_tower].append(towers[from_tower].pop())
            moves += 1
        else:
            print("Invalid move")
        if len(towers[2]) == 3:
            draw_towers(towers)
            print(f"You won in {moves} moves!")
            break

    if input("Play the Tower of Hanoi again? (y|n) ").lower() == "y":
        play_game()


if __name__ == "__main__":
    play_game()
    print("Bye!")
