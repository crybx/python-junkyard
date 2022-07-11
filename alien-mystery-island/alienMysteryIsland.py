import functions

#--------------------------------------------------------------------------------
# Game Setup
#--------------------------------------------------------------------------------
def setup(game):

        functions.welcome()

        game.getPlayersName()
        game.getCharacterChoice()
        game.getTotalPlayerCount()
        game.setUpPlayers()
        game.setUpSecretInfo()
        game.passOutHints()

        
#--------------------------------------------------------------------------------
# Play Time
#--------------------------------------------------------------------------------

game = functions.GameData()

setup(game)

game.showHintCards()

cards = game.players[game.playerChoice-1].hintCards

print ("----------------------------------------------")
print ("Type 'cards' to see your cards at any time.")
print ("Type 'game.move()' to move the current player's piece.")
print ("Type 'game.guess()' to get more clues.")
print ("Type 'game.accuse()' to make an accusation.")
