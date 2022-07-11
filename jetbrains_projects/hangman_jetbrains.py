import random
import sys


def play_game():
    print("H A N G M A N")

    word_list = ['python-junkyard', 'java', 'kotlin', 'javascript']
    word = random.choice(word_list)
    hint = list("-" * len(word))
    mistakes = 0
    win = False
    prior_guesses = set()

    while not win and mistakes < 8:
        print()
        print("".join(hint))
        guess = input("Input a letter:")

        if not is_input_valid(guess):
            continue
        elif guess in prior_guesses:
            print("You've already guessed this letter")
        elif guess in word:
            prior_guesses.add(guess)
            indices = [i for i, x in enumerate(word) if x == guess]
            for i in indices:
                hint[i] = word[i]
            if "-" not in hint:
                win = True
        else:
            mistakes += 1
            prior_guesses.add(guess)
            print("That letter doesn't appear in the word")

    if win:
        print()
        print("".join(hint))
        print(f"You guessed the word {word}!")
        print("You survived!")
    else:
        print("You lost!")


def is_input_valid(guess):
    if len(guess) > 1:
        print("You should input a single letter")
        return False
    elif not guess.isalpha() or not guess.islower():
        print("Please enter a lowercase English letter")
        return False
    else:
        return True


while True:
    player_choice = input('Type "play" to play the game, "exit" to quit:')
    if player_choice == "play":
        play_game()
    elif player_choice == "exit":
        sys.exit()
