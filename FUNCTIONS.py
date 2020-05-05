import PLAYER
import LOCATIONS
import ITEMS
import pickle
import math
import random

# CONSTANTS
SCREEN_CLEAR = 40
INC_HP_AMT = 5
INC_STR_AMT = 1
MAX_POT = 3  # Maximum allowed potions in inventory
TITLE_STRING = """

###     ###    ###    ###   ####  ######  ######### ######### #########
####   ####  ### ###  ####   ### ###   ## ######### ######### ##########
########### ###   ### #####  ### ###    # #  ###  # ###     # ###    ###
### ### ### ###   ### ###### ###  #####      ###    ####      ###    ###
###  #  ### ###   ### ### ######   #####     ###    ######    ########
###     ### ###   ### ###  ##### #    ###    ###    ####      ### ######
###     ### ###   ### ###   #### ##   ###    ###    ###     # ###    ###
####   ####  ### ###  ###    ###  ######    #####   ######### ###    ###
##### #####    ###    ####   ###   ####    #######  ######### ###   #####

    #########        ####    ######### ######### #####      #########
    ###   ####      ######   ######### #########  ###       #########
    ###     ###    ###  ###  #  ###  # #  ###  #  ###       ###     #
    ###   ####    ###    ###    ###       ###     ###       ####
    #######      ############   ###       ###     ###       ######
    ###    ####  #####  #####   ###       ###     ###       ####
    ###      ### ###      ###   ###       ###     ###     # ###     #
    ###   #####  ###      ###  #####     #####    ####  ### #########
    ########     ####    #### #######   #######  ########## #########
"""


def savePlayer(player):
    oFile = open('savePlayer.pickle', 'wb')
    pickle.dump(player, oFile)
    oFile.close()


def loadPlayer():
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
            return player


def levelUp(player):
    print(f'You can increase your HP by {INC_HP_AMT}, your STRENGTH ' +
          f'by {INC_STR_AMT}, or you can CANCEL.\n')
    while True:
        iString = whatToDo()
        if iString == 'hp':
            incHp(player)
            break
        if iString == 'strength':
            incStr(player)
            break
        elif iString == 'cancel':
            print('\nLevel up canceled.\n')
            break
        else:
            pleaseEnter(['hp', 'strength', 'cancel'])


def incStr(player):
    oldStr = player.strength
    player.strength += INC_STR_AMT
    player.experience -= player.levelUp()
    player.hp = player.maxHp
    player.level += 1
    print(f'\nYour strength went from {oldStr} to ' +
          f'{player.strength}.')
    print(f'You are now level {player.level}!\n')


def incHp(player):
    oldHp = player.maxHp
    player.maxHp += INC_HP_AMT
    player.hp = player.maxHp
    player.experience -= player.levelUp()
    player.level += 1
    print(f'\nYour maximum HP went from {oldHp} to ' +
          f'{player.maxHp}.')
    print(f'You are now level {player.level}!\n')


def whatToDo():
    iString = input('What would you like to do?\n')
    return iString.lower()


# Python doesn't allow function overloading. This is my work around
def pleaseEnter(option):  # option must be a list object
    numArgs = len(option)
    if numArgs == 2:
        print(f"Please enter '{option[0]}' or '{option[1]}'.\n")
    elif numArgs == 3:
        print(f"Please enter '{option[0]}', '{option[1]}', or " +
              f"'{option[2]}'.\n")
    elif numArgs == 4:
        print(f"Please enter '{option[0]}', '{option[1]}', " +
              f"'{option[2]}', or '{option[3]}'.\n")
    else:
        print(f'ERROR Edit pleaseEnter function to allow {numArgs} ' +
              f'arguments')


def getEnemy():
    enemy = random.choice(enemies.enemyList)
    enemy.hp = enemy.maxHp  # Enemy may have been damaged in previous battle
    enemy.alive = True
    return enemy


def notAvailable():
    print('\nThat feature is not available yet.\n')


def clearScreen():
    print('\n'*SCREEN_CLEAR)


def pressEnter():
    input('Press ENTER to continue.\n')


def printTitle(titleString):
    clearScreen()
    print(titleString)


def getPlayer():
    while True:
        choice = input('Would you like to create a character or load?\n')
        choice = choice.lower()
        if choice == 'create':
            name = input('What is your name?\n')
            player = PLAYER.Player(ITEMS.shortSword, 'human', 'knight',
                                   name, LOCATIONS.plaza)
            break
        elif choice == 'load':
            player = loadPlayer()
            break
        else:
            pleaseEnter(['create', 'load'])
    return player
