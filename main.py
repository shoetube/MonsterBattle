#!/usr/bin/python3
# Above tells program where to find python3.
'''
Library
    Done for now
Navigation
    Done for now
Store
    weapons, armor, recovery items
    focus on recovery items first to build in a bit of strategy
Arena
    option to flee
    gain experience and level up
    gain money to use in store
    #point based level up. increase attack and accuracy and hp
Fountain
    Done for now
'''
# IMPORTS
import sys
import pickle
import items
import enemies
from random import randint

# CONSTANTS
MAX_POT = 3  # Maximum allowed potions in inventory
TITLE_STRING = """

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
"""


###############################################################################
# CLASS DEFINITIONS                                                           #
###############################################################################
# Creature (parent)                                                           #
#                                                                             #
# --------------------------------------------------------------------------- #
# Player (child)                                                              #
#                                                                             #
# --------------------------------------------------------------------------- #
# Enemy (child)                                                               #
#                                                                             #
###############################################################################

class Creature:
    def __init__(self, weapon, race, job):
        self.weapon = weapon    # Player weapon is a class object
        self.race = race        # String
        self.job = job          # String
        self.alive = True


class Player(Creature):     # Player class used for user character
    def __init__(self, weapon, race, job, name):
        super().__init__(weapon, race, job)
        self.name = name        # Player name. String created from user input
        self.hp = 10            # Current health points
        self.maxHp = 10         # Maximum health points
        self.experience = 0     # Current experience points
        self.level = 1          # Current player level
        self.potion = items.potion
        self.numOfPot = 1


class Enemy(Creature):  # Create complex enemies. (Not in use)
    def __init__(self, weapon, race, job):
        super().__init__(weapon, race, job)
        pass

###############################################################################
# FUNCTION DEFINITIONS                                                        #
###############################################################################
# main                                                                        #
#                                                                             #
# Run main program                                                            #
#                                                                             #
# --------------------------------------------------------------------------- #
# notAvailable                                                                #
#                                                                             #
# Error message for undeveloped sections of program                           #
#                                                                             #
# --------------------------------------------------------------------------- #
# clearScreen                                                                 #
#                                                                             #
# Clear screen when entering new areas                                        #
#                                                                             #
# --------------------------------------------------------------------------- #
# printTitle                                                                  #
#                                                                             #
# Print title screen                                                          #
#                                                                             #
# --------------------------------------------------------------------------- #
# getPlayer                                                                   #
#                                                                             #
# Prompt player to create new character or load existing one                  #
#                                                                             #
# --------------------------------------------------------------------------- #
# plazaPrompt                                                                 #
#                                                                             #
# Central location where player starts and passes through to reach other      #
# locations. From here, the player can go to the arena, store, library or     #
# to the fountain.                                                            #
#                                                                             #
# --------------------------------------------------------------------------- #
# arenaPrompt                                                                 #
#                                                                             #
# Battle location. Accessed from the Plaza. Here the player can engage in     #
# battles for experience and currency to purchase items and equipment         #
#                                                                             #
# --------------------------------------------------------------------------- #
# battle                                                                      #
#                                                                             #
# Battle mode. Accessed through the arena. This is the main attraction of the #
# game.                                                                       #
#                                                                             #
# --------------------------------------------------------------------------- #
# storePrompt                                                                 #
#                                                                             #
# Store location. Accessed from the Plaza. Player can purchase items and      #
# equipment with currency gained from battling in the arena.                  #
#                                                                             #
# --------------------------------------------------------------------------- #
# libraryPrompt                                                               #
#                                                                             #
# Library location. Accessed from the Plaza. User can save or load a          #
# character from here or quit the game.                                       #
#                                                                             #
# --------------------------------------------------------------------------- #
# fountainPrompt                                                              #
#                                                                             #
# Fountain location. Accessed from the Plaza. User can check player           #
# information by looking at reflection or heal by drinking the water.         #
#                                                                             #
###############################################################################


def main():
    printTitle(TITLE_STRING)
    player = getPlayer()
    plazaPrompt(player)


# Place holder for undeveloped features
def notAvailable():
    print('\nThat feature is not available yet.\n')


# Fills screen with blank lines
def clearScreen():
    print('\n'*40)


def printTitle(titleString):
    clearScreen()
    print(titleString)
    input('Press ENTER to continue\n'.center(76))


def getPlayer():
    # Prompts user to create a new character or load an existing one.
    while True:
        choice = input('Would you like to create a character or load?\n')

        # CREATE
        if choice == 'create':
            name = input('What is your name?\n')
            player = Player(items.shortSword, 'human', 'knight', name)
            break

        # LOAD
        elif choice == 'load':

            # check if save file exists. If not, prompt to create new character
            isSaveFile = True
            try:
                iFile = open('savePlayer.pickle', 'rb')
            except IOError:
                print('\nNo save file to load\n')
                isSaveFile = False
            finally:
                if isSaveFile:
                    player = pickle.load(iFile)
                    iFile.close()
                    break

        # INVALID INPUT
        else:
            print("Plese enter 'create' or 'load'")

    return player


# Navigation and location functions
# Plaza - The central location from which the player can go to other areas.
def plazaPrompt(player):
    clearScreen()
    print('You are standing in the plaza.\n')
    print('The ARENA is to the WEST.')
    print('The STORE is to the NORTH.')
    print('The LIBRARY, to the EAST.')
    print('To the SOUTH, there is a  FOUNTAIN.\n')
    while True:     # Input checking
        iString = input('Where would you like to go?\n')
        iString = iString.lower()

        # ARENA
        if iString == 'arena' or iString == 'west':
            print('You go to the arena.')
            arenaPrompt(player)
            break

        # STORE
        elif iString == 'store' or iString == 'north':
            print('You go to the store.')
            storePrompt(player)
            break

        # LIBRARY
        elif iString == 'library' or iString == 'east':
            print('You go to the library')
            libraryPrompt(player)
            break

        # FOUNTAIN
        elif iString == 'fountain' or iString == 'south':
            fountainPrompt(player)
            print("please enter 'arena', 'store', 'library', or 'fountain'")


# Arena - The player can battle enemies here to gain experience
def arenaPrompt(player):
    clearScreen()
    print('You are in the arena.')
    print('You can BATTLE or EXIT to the plaza.')
    while True:     # Input checking
        iString = input('What would you like to do?\n')
        iString = iString.lower()

        # BATTLE
        if iString == 'battle':
            print('You have decided to battle.')
            battle(player)

        # GO TO PLAZA
        elif iString == 'exit' or iString == 'plaza':
            print('You have decided to go to exit to the plaza.')
            plazaPrompt(player)
            break
        print("Please enter 'battle' or 'exit'")


def battle(player):
    clearScreen()
    enemy = enemies.blueSlime
    print(f'{player.name} vs {enemy.name}!')
    battleRound = 1
    # reset state of enemy
    enemy.hp = enemy.maxHp
    enemy.alive = True

    # WHILE - battle loop
    while player.alive and enemy.alive:
        print(f'\nRemaining player health: {player.hp}/{player.maxHp}')
        print(f'Remaining enemy health: {enemy.hp}/{enemy.maxHp}')
        print('\nYou can ATTACK or HEAL')
        iString = input('What would you like to do?\n')
        clearScreen()
        print(f'Round {battleRound}')

        # ATTACK
        if iString == 'attack':
            print(f'You attack the {enemy.name} ' +
                  f'with you {player.weapon.name}.')
            atkDmg = randint(0, player.weapon.damage)
            # Player attacks enemy
            if atkDmg > 0:  # 0 damage is treated as a miss
                print(f'You hit the {enemy.name}. ' +
                      f'The {enemy.name} loses {atkDmg} hp.')
                enemy.hp -= atkDmg
            else:
                print(f'You miss the {enemy.name}.')

        # HEAL
        elif iString == 'heal':
            # If player has no potions, continue to beginning of loop
            if player.numOfPot < 1:
                print("You don't have any potions left")
                continue
            else:   # ELSE use potion
                items.potion.use(player)
                print(f'You have {player.numOfPot} potions left')

        # IF enemy alive, enemy attacks player
        if enemy.hp > 0:
            print(f'The {enemy.name} attacks you with its {enemy.weapon}.')
            atkDmg = randint(0, enemy.damage)

            # Enemy attacks player
            if atkDmg > 0:
                print(f'The {enemy.name} hits you. You lose {atkDmg} hp.')
                player.hp -= atkDmg
            else:
                print(f'The {enemy.name} misses you.')

            # Game ends if player reaches 0 HP
            if player.hp <= 0:
                print(f'You have been slain by the {enemy.name}.')
                player.alive = False
                input('\nGAME OVER.\n')
                sys.exit()

        # ENEMY DEFEATED
        else:
            print(f'You have slain the {enemy.name}.')
            enemy.alive = False
            input('\nPress ENTER to continue\n')

        battleRound += 1    # increment round number
    # END WHILE

    arenaPrompt(player)


def storePrompt(player):    # Store - buy and sell weapons and recovery items
    clearScreen()
    print('You are in the store.\n')
    print('You can BUY, SELL, or EXIT to the plaza\n')
    while True:     # Input checking
        iString = input('What would you like to do?\n')
        iString = iString.lower()

        # BUY
        if iString == 'buy':
            clearScreen()
            print('\nYou decide to buy.\n')
            print('Only potions are available now, but they are free!')
            print(f'You currently have {player.numOfPot} potions.')
            print(f'You can have up to {MAX_POT} in your inventory\n')
            buyInput = input('How many potions would you like?\n')

            # How many potions does the player want?
            if buyInput.isdigit():
                numToBuy = int(buyInput)

                # If the player can carry that many...
                if numToBuy + player.numOfPot <= MAX_POT:
                    print(f'Here you go!')
                    player.numOfPot += numToBuy

                # If the player cannot carry any more potions...
                elif player.numOfPot >= MAX_POT:
                    print("\nYou can't carry any more potions!")

                # If the player can carry some of them...
                else:
                    numToBuy = MAX_POT - player.numOfPot
                    print("\nYou can't carry that many!")
                    print(f'I will give you {numToBuy} potions instead.')
                    player.numOfPot += numToBuy

            # return to store prompt after purchase
            input('\npress ENTER to continue\n')
            storePrompt(player)
            break

        # SELL
        elif iString == 'sell':
            clearScreen()
            print('\nYou decide to sell.')
            notAvailable()      # Needs development
            input('\npress ENTER to continue\n')
            storePrompt(player)
            break

        # GO TO PLAZA
        elif iString == 'exit' or iString == 'plaza':
            print('You have decided to exit to the plaza.')
            plazaPrompt(player)
            break

        # INVALID INPUT
        else:
            print("\nPlease enter 'buy', 'sell', or 'exit'.\n")


# Library - Save or load character data and quit game. A utility area.
def libraryPrompt(player):
    clearScreen()
    print('You are in the library.')
    print('You can SAVE, LOAD, QUIT the game, or EXIT to the plaza')

    while True:     # Input checking
        iString = input('What would you like to do?\n')

        # SAVE
        if iString == 'save':
            print('You have decided to save.')
            oFile = open('savePlayer.pickle', 'wb')
            pickle.dump(player, oFile)
            oFile.close()
            print('\nSave successful!\n')

        # LOAD
        elif iString == 'load':
            print('You have decided to load.')
            isSaveFile = True
            try:
                iFile = open('savePlayer.pickle', 'rb')
            except IOError:
                print('\nNo save file to load\n')
                isSaveFile = False
            finally:
                if isSaveFile:
                    player = pickle.load(iFile)
                    iFile.close()
                    print('\nLoad successful!\n')
                    print('Welcome, ' + player.name)

        # QUIT THE GAME
        elif iString == 'quit':
            print('You have decided to quit the game.')
            sys.exit()

        # GO TO THE PLAZA
        elif iString == 'exit' or iString == 'plaza':
            print('You have decided to exit to the plaza.')
            plazaPrompt(player)
            break

        # INVALID INPUT
        else:
            print("please enter 'save', 'load', 'quit', or 'exit'.")


def fountainPrompt(player):     # Examine player character information
    clearScreen()
    print('You are at the fountain.\n')
    print('You can LOOK at your reflection,')
    print('you can DRINK from the fountain,')
    print('you can EXIT to the plaza.\n')
    while True:     # Input checking
        iString = input('What would you like to do?\n')
        iString = iString.lower()

        # LOOK at reflection
        if iString == 'look':
            clearScreen()
            print('\nYou look at your reflection in the water of the fountain')
            print(f'You are {player.name}. A {player.race} {player.job} ' +
                  f'wielding a {player.weapon.name}.')
            print(f'You have {player.hp} of {player.maxHp}.')
            print(f'You are carrying {player.numOfPot} potions.')
            input('\npress ENTER to continue\n')
            fountainPrompt(player)
            break

        # DRINK from fountain
        elif iString == 'drink':
            clearScreen()
            print('\nYou drink from the fountain.')
            player.hp = player.maxHp
            print('Your HP is restored.')
            input('\npress ENTER to continue\n')
            fountainPrompt(player)
            break

        # GO TO PLAZA
        elif iString == 'exit' or iString == 'plaza':
            print('You have decided to go to exit to the plaza.')
            plazaPrompt(player)
            break

        # INVALID INPUT
        else:
            print("Please enter 'look', 'drink', or 'exit'")


main()
