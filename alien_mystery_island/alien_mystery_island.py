import functions


def welcome():
    print("""
                        Welcome to...
            A L I E N   M Y S T E R Y   I S L A N D

        You are a member of a team of explorers who have been 
    sent to a remote island to investigate a series of strange 
    events.
        You have been told that the island is inhabited
    by aliens, and that they have been abducting people from
    the island. Your mission is to find out what is going on,
    and to rescue any people who have been abducted.
        You will be given a list of people, items, and locations
    on the island. You will also be given a list of secret 
    information that only you know.
        You will be able to move around the island, and make 
    guesses about what is going on. You will be able to ask 
    other players for hints about what is going on.
        You will be able to accuse other players of being aliens.
        If you are wrong, you will be abducted by the aliens and 
    the game will be over. If you are right, you will be able to 
    rescue the abducted people.
    """)


def setup(game):
    """Game Setup"""
    welcome()

    game.get_player_name()
    game.get_character_choice()
    game.get_total_player_count()
    game.setup_players()
    game.setup_secret_info()
    game.pass_out_hints()


def play_game():
    game = functions.GameData()
    setup(game)
    game.show_hint_cards()

    cards = game.players[game.player_choice - 1].hint_cards

    print("----------------------------------------------")
    print("Type 'cards' to see your cards at any time.")
    print("Type 'game.move()' to move the current player's piece.")
    print("Type 'game.guess()' to get more clues.")
    print("Type 'game.accuse()' to make an accusation.")


if __name__ == "__main__":
    play_game()
