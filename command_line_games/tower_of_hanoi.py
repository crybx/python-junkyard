
def create_towers():
    return [[3, 2], [3, 2, 1], []]


def draw_towers(towers):
    for i in range(len(towers)):
        print(f"tower {i + 1}")
        for ring in towers[i]:
            print(ring)


def draw_towers_again(towers):
    # going to draw things a bit funky
    # draw top row first
    empty = f"     |||      "
    row1 = "   [=|||=]    "
    row2 = "  [==|||==]   "
    row3 = " [===|||===]  "
    print(row1)
    print(row2)
    print(row3)
    print(" ---- 1 ----   ---- 2 ----   ---- 3 ---- ")


def play_game():
    towers = create_towers()
    draw_towers_again(towers)


play_game()
