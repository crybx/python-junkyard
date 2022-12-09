import random


class Player:
    def __init__(self, is_npc, player_name, start_location):
        self.is_npc = is_npc
        self.name = player_name
        self.hint_cards = []
        self.location = start_location


class Location:
    def __init__(self, location_name, reachable):
        self.name = location_name
        self.reachable = reachable


class GameData:
    people = [
        "The Ranger",
        "The Scientist",
        "The Tourist",
        "The Grandpa",
        "The Duchess",
        "The CEO"
    ]
    item_list = [
        "Stick doll",
        "Pendant",
        "Old bone",
        "Island map",
        "Shiny orb",
        "Coin"
    ]
    locations = []
    player_name = None
    current_player = None
    
    players = []
    player_choice = 1
    player_count = 6

    special_person = None
    special_item = None
    special_location = None
    special_combo_list = []

    def __init__(self):
        beach = "Beach"
        village = "Village"
        caves = "Caves"
        
        banana = "Banana grove"
        altar = "The altar"
        firepit = "Fire pit"
        
        cliff = "Clifftop"
        waterfall = "Waterfall"
        river = "Riverbank"
        
        self.locations.append(Location(beach, [village, river, altar]))
        self.locations.append(Location(village, [caves, beach]))
        self.locations.append(Location(caves, [village, banana, cliff]))

        self.locations.append(Location(banana, [caves, altar]))
        self.locations.append(Location(altar, [banana, firepit, beach]))
        self.locations.append(Location(firepit, [altar, cliff]))

        self.locations.append(Location(cliff, [firepit, waterfall, caves]))
        self.locations.append(Location(waterfall, [cliff, river]))
        self.locations.append(Location(river, [waterfall, beach]))

    def get_player_name(self):
        self.player_name = input("What's your name? ")

    def get_character_choice(self):
        print("--------------------------------")
        print('Hi %s.' % self.player_name, "Which character would you like to be?")

        # print the list of playable people like "1 - The Ranger"
        for item in self.people:
            print(self.people.index(item) + 1, "-", item)

        self.player_choice = int(input("Enter the number of your choice: "))

    def get_total_player_count(self):
        print("--------------------------------")
        self.player_count = int(input("Enter the total number of players you want to play (3-6): "))

    def setup_players(self):
        # set up the list of who will be playing
        for person in self.people:
            location = random.choice(self.locations)

            # args for Player() - isNPC, name, location
        
            if self.player_choice == self.people.index(person) + 1:
                # this is the human's choice of character
                self.players.append(Player(False, person, location))
            else:
                player_count = len(self.players)
                if player_count + 1 < self.player_count:
                    self.players.append(Player(True, person, location))
                elif player_count < self.player_count and not self.player_choice > self.player_count:
                    self.players.append(Player(True, person, location))

        self.current_player = self.players[0]

    def setup_secret_info(self):
        # choose the secret information
        self.special_person = random.choice(self.people)
        self.special_item = random.choice(self.item_list)
        self.special_location = random.choice(self.locations)
        self.special_combo_list = [self.special_person, self.special_item, self.special_location]

    def pass_out_hints(self):
        deck = []

        # building the deck of hint cards to pass out to the players
        # (that doesn't include the secret info)
        for person in self.people:
            if person == self.special_person:
                continue
            else:
                deck.append(person)

        for item in self.item_list:
            if item == self.special_item:
                continue
            else:
                deck.append(item)

        for loc in self.locations:
            if loc == self.special_location:
                continue
            else:
                deck.append(loc.name)

        # shuffle the deck twice
        random.shuffle(deck)
        random.shuffle(deck)
        
        # pass cards out to the players
        while len(deck) != 0:
            card = deck.pop()
            self.current_player.hint_cards.append(card)
            self.set_next_player()

        # reset the first player
        self.set_first_player()

    def set_next_player(self):
        current_index = self.players.index(self.current_player)
        new_index = 0
        
        if self.player_count - 1 != current_index:
            new_index = current_index + 1

        self.current_player = self.players[new_index]

    def set_first_player(self):
        self.current_player = self.players[0]

    def show_hint_cards(self):
        print("----------------------------")
        print("These are your hint cards:")
        player = self.players[self.player_choice - 1]

        index = 1
        for card in player.hint_cards:
            print(index, "-", card)
            index += 1

    def move(self):
        player = self.current_player
        
        print("----------------------------")
        print(player.name, 'is currently located at the %s.' % player.location.name,)
        print("Where would you like to move?")

        # show available moves
        number = 1
        for place in player.location.reachable:
            print(number, "-", place)
            number += 1

        # get the user's move choice
        print("----------------------------")
        choice = int(input("Enter the number of your choice: "))
        new_location_name = player.location.reachable[choice - 1]

        # set new location
        for loc in self.locations:
            if loc.name == new_location_name:
                player.location = loc
                break

        print("You chose:", new_location_name)

    def guess(self):
        player = self.current_player
        
        print("----------------------------")
        print(player.name, 'is currently located at the %s.' % player.location.name,)

        # show available items
        print("----------------------------")
        print("The items available to choose from are:")

        number = 1
        for item in self.item_list:
            print(number, "-", item)
            number += 1

        # get the user's choice of item
        print("----------------------------")
        choice = int(input("Enter the number of your choice: "))
        item_picked = self.item_list[choice - 1]

        # show available people
        print("----------------------------")
        print("The people available to choose from are:")

        number = 1
        for person in self.people:
            print(number, "-", person)
            number += 1
        
        # get the user's choice of person
        print("----------------------------")
        choice = int(input("Enter the number of your choice: "))
        person_picked = self.people[choice - 1]

        # check the next player's cards to see if they have any of the choices
        self.check_against_cards(player.location, item_picked, person_picked, player)
        
        # keep checking until someone has a card to show
        # reveal that card
        # update AI info

    def check_against_cards(self, location, item, person, player):
        # randomize the order of what we are checking so that
        # one type of card isn't always revealed first
        guesses = [location.name, item, person]
        random.shuffle(guesses)

        # start with the index of the very next player
        idx = (self.players.index(player) + 1) % len(self.players)

        count = self.player_count - 1
        while count != -1:
            if count == 0:
                print("No one can disprove your claim.")
                break

            helper = self.players[idx]
            
            # check the cards
            for guess in guesses:
                if guess in helper.hint_cards:
                    print(helper.name, "has the card", guess)
                    count = -1
                    break
            
            # increment to the next player to check
            idx = (idx + 1) % len(self.players)

    def accuse(self, location, item, person):
        # check if the accusation is correct
        if location == self.special_location and item == self.special_item and person == self.special_person:
            print("You win!")
            return True
        else:
            print("You lose!")
            return False
