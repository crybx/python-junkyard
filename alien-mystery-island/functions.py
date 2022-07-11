from __future__ import print_function
import random

class Player:
    def __init__(self, isNPC, playerName, startLoc):
        self.isNPC = isNPC
        self.name = playerName
        self.hintCards = []
        self.location = startLoc

class Location:
    def __init__(self, locName, reachable):
        self.name = locName
        self.reachable = reachable

class GameData:
    people = ["The Ranger", "The Scientist", "The Hippie", "The Grandpa",
                  "The Dutchess", "The CEO"]
    itemList = ["Stick doll", "Pendant", "Old bone",
                "Island map", "Shiny orb", "Coin"]
    locations = []

    playersName = None
    currentPlayer = None
    
    players = []
    playerChoice = 1
    playerCount = 6

    specialComboList = []
    specialPerson = None
    specialItem = None
    specialLocation = None

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


    #--------------------------------------------------------------------------------
    def getPlayersName(self):
        self.playersName = raw_input("So what\'s your name? ")
        return

    #--------------------------------------------------------------------------------
    def getCharacterChoice(self):
        print("--------------------------------")
        print('Hi %s.' % self.playersName, "Which character would you like to be?")

        #printing out the list of playable people like "1 - The Ranger"
        for item in self.people:
            print( self.people.index(item)+1, "-", item )

        self.playerChoice = int(raw_input("Enter the number of your choice: "))
        return
    
    #--------------------------------------------------------------------------------
    def getTotalPlayerCount(self):
        print("--------------------------------")
        self.playerCount = int(raw_input("Enter the total number of players you want to play (3-6): "))
        return

    #--------------------------------------------------------------------------------
    def setUpPlayers(self):
        #set up the list of who will be playing
        for person in self.people:
            location = random.choice(self.locations)

            #args for Player() - isNPC, name, location
        
            if(self.playerChoice == self.people.index(person) + 1):
                    #this is the human's choice of character
                    self.players.append(Player(False, person, location))
                
            else:
                    if len(self.players) + 1 < self.playerCount:
                            self.players.append(Player(True, person, location))
                    elif (len(self.players) < self.playerCount
                          and not self.playerChoice > self.playerCount):
                            self.players.append(Player(True, person, location))

        self.currentPlayer = self.players[0]

        return

    #--------------------------------------------------------------------------------
    def setUpSecretInfo(self):
        #choosing the secret information
        self.specialPerson = random.choice(self.people)
        self.specialItem = random.choice(self.itemList)
        self.specialLocation = random.choice(self.locations)

        self.specialComboList = [self.specialPerson, self.specialItem, self.specialLocation]
        return
    
    #--------------------------------------------------------------------------------
    def passOutHints(self):
        deck = []

        #building the deck of hint cards to pass out to the players
        #(that doesn't include the secret info)
        for person in self.people:
            if person == self.specialPerson:
                continue
            else:
                deck.append(person)

        for item in self.itemList:
            if item == self.specialItem:
                continue
            else:
                deck.append(item)

        for loc in self.locations:
            if loc == self.specialLocation:
                continue
            else:
                deck.append(loc.name)

        #shuffling the cards
        random.shuffle(deck)
        #twice is better?
        random.shuffle(deck)
        
        #passing the cards out to the players
        while len(deck) != 0:
            card = deck.pop()
            self.currentPlayer.hintCards.append(card)
            self.setNextPlayer()

        #resetting the first player
        self.setFirstPlayer()

        return

    #--------------------------------------------------------------------------------
    def setNextPlayer(self):
        currentIndex = self.players.index(self.currentPlayer)
        newIndex = 0
        
        if self.playerCount - 1 != currentIndex:
                newIndex = currentIndex + 1

        self.currentPlayer = self.players[newIndex]

    #--------------------------------------------------------------------------------
    def setFirstPlayer(self):
        self.currentPlayer = self.players[0]

    #--------------------------------------------------------------------------------
    def showHintCards(self):
        print("----------------------------")
        print("These are your hint cards:")
        player = self.players[self.playerChoice-1]

        index = 1
        for card in player.hintCards:
            print(index, "-", card)
            index += 1

    #---------------------------------------------------------------------------       
    def move(self):
        player = self.currentPlayer
        
        print("----------------------------")
        print(player.name, 'is currently located at the %s.' % player.location.name,)
        print("Where would you like to move?")

        #show available moves
        number = 1
        for place in player.location.reachable:
            print(number, "-", place)
            number += 1

        #get the user's move choice
        print("----------------------------")
        choice = int(raw_input("Enter the number of your choice: "))
        newLocName = player.location.reachable[choice - 1]

        #set new location
        for loc in self.locations:
            if loc.name == newLocName:
                player.location = loc
                break

        print("You chose:", newLocName)
        
	
    #--------------------------------------------------------------------------------
    def guess(self):
        player = self.currentPlayer
        
        print("----------------------------")
        print(player.name, 'is currently located at the %s.' % player.location.name,)

        #show available items
        print("----------------------------")
        print("The items available to choose from are:")

        number = 1
        for item in self.itemList:
            print(number, "-", item)
            number += 1

        #get the user's choice of item
        print("----------------------------")
        choice = int(raw_input("Enter the number of your choice: "))
        itemPicked = self.itemList[choice - 1]

        #show available people
        print("----------------------------")
        print("The people available to choose from are:")

        number = 1
        for person in self.people:
            print(number, "-", person)
            number += 1
        
        #get the user's choice of person
        print("----------------------------")
        choice = int(raw_input("Enter the number of your choice: "))
        personPicked = self.people[choice - 1]

        #check the next player's cards to see if they have any of the choices
        self.checkAgainstCards(player.location, itemPicked, personPicked, player)
        
        #keep checking until someone has a card to show
        #reveal that card
        #update AI info

    def checkAgainstCards(self, location, item, person, player):
        #randomize the order of what we are checking so that
        #one type of card isn't always revealed first
        guesses = [location.name, item, person]
        random.shuffle(guesses)

        #start with the index of the very next player
        idx = (self.players.index(player) + 1) % len(self.players)

        count = self.playerCount - 1
        while count != -1:
            if count == 0:
                print("No one can disprove your claim.")
                break

            helper = self.players[idx]
            
            #check the cards
            for guess in guesses:
                if guess in helper.hintCards:
                    print(helper.name, "has the card", guess)
                    count = -1
                    break
            
            #increment to the next player to check
            idx = (idx + 1) % len(self.players)
        
        return
		
    #--------------------------------------------------------------------------------
    def accuse(self):
        print("Not ready")



def welcome():
    print ('Welcome to Alien Mystery Island...')
    return


