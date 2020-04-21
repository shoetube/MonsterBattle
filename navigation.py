#!/usr/bin/python3 
# Above tells program where to find python3. Necessary to make program executable

'''
Archives
   Done for now
Navigation
   Done for now
Store
   weapons, armor, recovery items
   focus on recovery items first to build in a bit of strategy
Arena
    gain experience and level up
       #point based level up. increase attack and accuracy and hp
   Monsters don't need to be nearly as complex as the player.
   Why not make a simply slime enemy?
   I can create several simple enemies of varying difficulty easily.
   Need to create a file with various monsters in it.
'''
# sys to exit game and pickle for saving and loading of player character data
import sys, pickle, items

# Creature parent class.
class Creature:
    def __init__(self, weapon, race, job):
        self.weapon = weapon # Player weapon is an object with its own properties
        self.race   = race   # String
        self.job    = job    # String
        self.alive  = True

class Player(Creature): # Player class used for user character
    def __init__(self, weapon, race, job, name):
        super().__init__(weapon, race, job)
        self.name       = name   # Player name. A string created from user input
        self.hp         = 10     # Current health points
        self.maxHp      = 10     # Maximum health points
        self.experience = 0      # Current experience points
        self.level      = 1      # Current player level

class Enemy(Creature): # create complex enemies for player to fight in arena
    def __init__(self, weapon, race, job):
        super().__init__(weapon, race, job)
        pass

# Navigation and location functions
def plazaPrompt(player): # Plaza - The central location from which the player can go to other areas.
    clearScreen()
    print('You are standing in the plaza.\n')
    print('The ARENA is to the WEST.')
    print('The STORE is to the NORTH.')
    print('The LIBRARY, to the EAST.')
    print('To the SOUTH, there is a  FOUNTAIN.\n')
    while True: # Input checking
        iString = input('Where would you like to go?\n')
        iString = iString.lower()
        if iString == 'arena' or iString == 'west':
            print('You go to the arena.')
            arenaPrompt(player)
            break
        elif iString == 'store' or iString == 'north':
            print('You go to the store.')
            storePrompt(player)
            break
        elif iString == 'library' or iString == 'east':
            print('You go to the library')
            libraryPrompt(player)
            break
        elif iString == 'fountain' or iString == 'south':
            fountainPrompt(player)
        print("please enter 'arena', 'store', 'library', or 'fountain'")

def arenaPrompt(player): # Arena - The player can battle enemies here to gain experience
    clearScreen()
    print('You are in the arena.')
    print('You can BATTLE or EXIT to the plaza.')
    while True: # Input checking
        iString = input('What would you like to do?\n')
        iString = iString.lower()
        if iString == 'battle':
            print('You have decided to battle.')
            notAvailable()  # Needs development
        elif iString == 'exit' or iString == 'plaza':
            print('You have decided to go to exit to the plaza.')
            plazaPrompt(player)
            break
        print("Please enter 'battle' or 'exit'")

def storePrompt(player): # Store - buy and sell weapons and recovery items
    clearScreen()
    print('You are in the store.')
    print('You can BUY, SELL, or EXIT to the plaza')
    while True: # Input checking
        iString = input('What would you like to do?\n')
        iString = iString.lower()
        if iString == 'buy':
            print('You decide to buy.')
            notAvailable()  # Needs development
        elif iString == 'sell':
            print('You decide to sell.')
            notAvailable()  # Needs development
        elif iString == 'exit' or iString == 'plaza':
            print('You have decided to exit to the plaza.')
            plazaPrompt(player)
            break
        print("Please enter 'buy', 'sell', or 'exit'.")

def libraryPrompt(player): # Library - Save or load character data and quit game. A utility area.
    clearScreen()
    print('You are in the library.')
    print('You can SAVE, LOAD, QUIT the game, or EXIT to the plaza')
    while True: # Input checking
        iString = input('What would you like to do?\n')
        if iString == 'save':
            print('You have decided to save.')
            oFile = open('savePlayer.pickle', 'wb')
            pickle.dump(player, oFile)
            oFile.close()
            print('Save successful!')
        elif iString == 'load':
            print('You have decided to load.')
            iFile = open('savePlayer.pickle', 'rb')
            player = pickle.load(iFile)
            iFile.close()
            print('Load successful!')
            print('Welcome, ' + player.name)
        elif iString == 'quit':
            print('You have decided to quit the game.')
            sys.exit()
        elif iString == 'exit' or iString == 'plaza':
            print('You have decided to exit to the plaza.')
            plazaPrompt(player)
            break
        else:
            print("please enter 'save', 'load', 'quit', or 'exit'.")

def fountainPrompt(player): # Examine player character information
    print('You look at your reflection in the water of the fountain')
    print(f'You are {player.name}. A {player.race} {player.job} wielding a {player.weapon.name}.')
    input('press ENTER to continue\n')
    plazaPrompt(player)

# Place holder for undeveloped features
def notAvailable():
    print('\nThat feature is not available yet.\n')

# Fills screen with blank lines
def clearScreen():
    print('\n'*40)

# Begin game
clearScreen()
print("""

###     ###     ###    ###   ####   ######   ######### ######### #########
####   ####   ### ###  ####   ###  ###   ##  ######### ######### ##########
###########  ###   ### #####  ###  ###    #  #  ###  # ###     # ###    ###
### ### ###  ###   ### ###### ###   #####       ###    ####      ###    ###
###  #  ###  ###   ### ### ######    #####      ###    ######    ########
###     ###  ###   ### ###  #####  #    ###     ###    ####      ### ######
###     ###  ###   ### ###   ####  ##   ###     ###    ###     # ###    ###
####   ####   ### ###  ###    ###   ######     #####   ######### ###    ###
##### #####     ###    ####   ###    ####     #######  ######### ###   #####

     #########        ####     ######### ######### #####      #########
     ###   ####      ######    ######### #########  ###       #########
     ###     ###    ###  ###   #  ###  # #  ###  #  ###       ###     #
     ###   ####    ###    ###     ###       ###     ###       ####     
     #######      ############    ###       ###     ###       ######   
     ###    ####  #####  #####    ###       ###     ###       ####     
     ###      ### ###      ###    ###       ###     ###     # ###     #
     ###   #####  ###      ###   #####     #####    ####  ### #########
     ########     ####    ####  #######   #######  ########## #########
""")
input('                        Press ENTER to continue\n')
while True:
    choice = input('Would you like to create a character or load?\n')
    if choice == 'create':
        name   = input('What is your name?\n')
        player = Player(items.shortSword, 'human', 'knight', name)
        break
    elif choice == 'load':
        iFile  = open('savePlayer.pickle', 'rb')
        player = pickle.load(iFile)
        iFile.close()
        break
    else:
        print("Plese enter 'create' or 'load'")

plazaPrompt(player) 
