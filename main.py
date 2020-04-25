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
    make player method for using potions. too messy doing it procedurally.
Arena
    gain experience and level up
    #point based level up. increase attack and accuracy and hp
Fountain
    drink from fountain to heal
'''
# sys to exit game and pickle for saving and loading of player character data
import sys
import pickle
import items
import enemies
from random import randint

MAX_POT = 3  # Maximum allowed potions in inventory


# Creature parent class.
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


# Arena - The player can battle enemies here to gain experience
def arenaPrompt(player):
    clearScreen()
    print('You are in the arena.')
    print('You can BATTLE or EXIT to the plaza.')
    while True:     # Input checking
        iString = input('What would you like to do?\n')
        iString = iString.lower()
        if iString == 'battle':
            print('You have decided to battle.')
            battle(player)
        elif iString == 'exit' or iString == 'plaza':
            print('You have decided to go to exit to the plaza.')
            plazaPrompt(player)
            break
        print("Please enter 'battle' or 'exit'")


def battle(player):
    clearScreen()
    enemy = enemies.blueSlime
    e = enemy
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
        # engage first round of attacks
        if iString == 'attack':
            print(f'You attack the {e.name} with you {player.weapon.name}.')
            atkDmg = randint(0, player.weapon.damage)

            # Player attacks enemy
            if atkDmg > 0:  # 0 damage is treated as a miss
                print(f'You hit the {e.name}. The {e.name} loses {atkDmg} hp.')
                enemy.hp -= atkDmg
            else:
                print(f'You miss the {e.name}.')

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

        else:
            print(f'You have slain the {enemy.name}.')
            enemy.alive = False
            input('\nPress ENTER to continue\n')

        battleRound += 1    # increment round number
    # END WHILE

    arenaPrompt(player)


def storePrompt(player):    # Store - buy and sell weapons and recovery items
    clearScreen()
    print('You are in the store.')
    print('You can BUY, SELL, or EXIT to the plaza')
    while True:     # Input checking
        iString = input('What would you like to do?\n')
        iString = iString.lower()
        if iString == 'buy':
            print('\nYou decide to buy.')
            print('Only potions are available now, but they are free!')
            print(f'You can have up to {MAX_POT} in your inventory')
            buyInput = input('How many potions would you like?\n')

            if buyInput.isdigit():
                numToBuy = int(buyInput)

                if numToBuy + player.numOfPot <= MAX_POT:
                    print(f'Here you go!')
                    player.numOfPot += numToBuy
                elif player.numOfPot >= MAX_POT:
                    print("You can't carry any more potions!")
                else:
                    numToBuy = MAX_POT - player.numOfPot
                    print("You can't carry that many!")
                    print(f'I will give you {numToBuy} potions instead.')
                    player.numOfPot += numToBuy
        elif iString == 'sell':
            print('You decide to sell.')
            notAvailable()      # Needs development
        elif iString == 'exit' or iString == 'plaza':
            print('You have decided to exit to the plaza.')
            plazaPrompt(player)
            break
        print("Please enter 'buy', 'sell', or 'exit'.")


# Library - Save or load character data and quit game. A utility area.
def libraryPrompt(player):
    clearScreen()
    print('You are in the library.')
    print('You can SAVE, LOAD, QUIT the game, or EXIT to the plaza')
    while True:     # Input checking
        iString = input('What would you like to do?\n')
        if iString == 'save':
            print('You have decided to save.')
            oFile = open('savePlayer.pickle', 'wb')
            pickle.dump(player, oFile)
            oFile.close()
            print('\nSave successful!\n')
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
        elif iString == 'quit':
            print('You have decided to quit the game.')
            sys.exit()
        elif iString == 'exit' or iString == 'plaza':
            print('You have decided to exit to the plaza.')
            plazaPrompt(player)
            break
        else:
            print("please enter 'save', 'load', 'quit', or 'exit'.")


def fountainPrompt(player):     # Examine player character information
    clearScreen()
    p = player                  # shorten player for formatting purposes
    print('\nYou look at your reflection in the water of the fountain')
    print(f'You are {p.name}. A {p.race} {p.job} wielding a {p.weapon.name}.')
    input('\npress ENTER to continue\n')
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
input('Press ENTER to continue\n'.center(76))

# Prompts user to create a new character or load an existing one.
while True:
    choice = input('Would you like to create a character or load?\n')
    if choice == 'create':
        name = input('What is your name?\n')
        player = Player(items.shortSword, 'human', 'knight', name)
        break
    elif choice == 'load':
        # check if save file exists. If not, prompt to create a new character
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
    else:
        print("Plese enter 'create' or 'load'")
# send player to the plaza
plazaPrompt(player)
