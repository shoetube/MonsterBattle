import PLAYER
import LOCATIONS
import ENEMIES
import ITEMS
import pickle
import math
import random
import sys

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
            player.maxHp = incStat(player, player.maxHp,
                                   INC_HP_AMT, 'maximum HP')
            player.hp = player.maxHp
            break
        if iString == 'strength':
            player.strength = incStat(player, player.strength,
                                      INC_STR_AMT, 'strength')
            break
        elif iString == 'cancel':
            print('\nLevel up canceled.\n')
            break
        else:
            pleaseEnter(['hp', 'strength', 'cancel'])


def incStat(player, stat, incAmt, statName):
    clearScreen()
    oldStat = stat
    stat += incAmt
    player.hp = player.maxHp
    player.experience -= player.levelUp()
    player.level += 1
    print(f'\nYour {statName} went from {oldStat} to ' +
          f'{stat}.')
    print(f'You are now level {player.level}!\n')
    return stat


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
    enemy = random.choice(ENEMIES.enemyList)
    enemy.hp = enemy.maxHp
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
        choice = input('Would you like to (C)REATE a character or ' +
                       '(L)OAD?\n')
        choice = choice.lower()
        if choice == 'create' or choice == 'c':
            name = input('\nWhat is your name?\n')
            player = PLAYER.Player(ITEMS.shortSword, 'human', 'knight',
                                   name, LOCATIONS.plaza)
            break
        elif choice == 'load' or choice == 'l':
            player = loadPlayer()
            break
        else:
            pleaseEnter(['create', 'load'])
    return player


def battle(player):
    clearScreen()
    enemy = getEnemy()
    print(f'{player.name} vs {enemy.name}!')
    battleRound = 1
    battleLoop(player, enemy, battleRound)


def battleLoop(player, enemy, battleRound):
    iString = batLoopPrompt(player, enemy, battleRound)
    if iString == 'attack' or iString == 'a':
        player.attack(enemy)
    elif iString == 'heal' or iString == 'h':
        healPotion(player, enemy, battleRound)
    elif iString == 'surrender' or iString == 's':
        surrender(player, enemy, battleRound)
    else:                       # INVALID INPUT
        battleLoop(player, enemy, battleRound)
    if enemy.hp > 0:            # If enemy alive, enemy attacks
        enemy.attack(player)
        if player.hp <= 0:      # Player defeated
            defeatPlayer(player, enemy)
    else:                       # Enemy defeated
        defeatEnemy(player, enemy)
    battleRound += 1
    battleLoop(player, enemy, battleRound)


def defeatPlayer(player, enemy):
    print(f'You have been slain by the {enemy.name}.')
    player.alive = False
    input('\nGAME OVER.\n')
    sys.exit()


def defeatEnemy(player, enemy):
    print(f'You have slain the {enemy.name}.')
    enemy.alive = False
    player.experience += enemy.grantExp
    gainGold = enemy.dropGold()
    player.gold += gainGold
    print(f'\nYou gain {enemy.grantExp} experience.')
    print(f'You found {gainGold} pieces of gold.\n')
    pressEnter()
    player.query()


def healPotion(player, enemy, battleRound):
    # If player has no potions, continue to beginning of loop
    if player.numOfPot < 1:
        print("You don't have any potions left")
        battleLoop(player, enemy, battleRound)
    else:   # ELSE use potion
        ITEMS.potion.use(player)
        print(f'You have {player.numOfPot} potions left')


def surrender(player, enemy, battleRound):
    LOSE_EXP_SURRENDER = player.experience // 3
    print(f'If you surrender, you will lose ' +
          f'{LOSE_EXP_SURRENDER} experience.\n')
    surrenderLoop(player, enemy, battleRound,
                  LOSE_EXP_SURRENDER)


def batLoopPrompt(player, enemy, battleRound):
    print(f'\nRound {battleRound}')
    print(f'\nRemaining player health: {player.hp}/{player.maxHp}')
    print(f'Remaining enemy health: {enemy.hp}/{enemy.maxHp}')
    print('\nYou can (A)ttack, (H)eal, or (S)urrender.\n')
    iString = whatToDo()
    clearScreen()
    return iString


def surrenderLoop(player, enemy, battleRound,
                  LOSE_EXP_SURRENDER):
    choice = input('Are you sure that you want to surrender?\n')
    choice = choice.lower()
    if choice == 'yes' or choice == 'y':
        clearScreen()
        oldExp = player.experience
        player.experience -= LOSE_EXP_SURRENDER
        print(f'\nYour experience points went from ' +
              f'{oldExp} to {player.experience}.\n')
        pressEnter()
        player.query()
    elif choice == 'no' or choice == 'n':
        clearScreen()
        battleLoop(player, enemy, battleRound)
    else:
        clearScreen()
        pleaseEnter(['yes', 'no'])
        surrenderLoop(player, enemy, battleRound,
                      LOSE_EXP_SURRENDER)


def buy(player):
    potionCost = 2
    clearScreen()
    print(f'You can buy potions for {potionCost} gold each.')
    print(f'You currently have {player.gold} gold.\n')
    print(f'You currently have {player.numOfPot} potions.')
    print(f'You can have up to {MAX_POT} in your inventory.\n')

    if player.numOfPot >= MAX_POT:
        print("You can't carry any more potions!\n")
        pressEnter()
        player.query()
    buyInput = input('How many potions would you like?\n')

    # How many potions does the player want?
    if buyInput.isdigit():
        quantity = int(buyInput)
        totalCost = quantity * potionCost

        # If player can afford that many
        if player.gold >= totalCost:

            # If player can hold that many
            if player.numOfPot + quantity <= MAX_POT:
                player.gold -= totalCost
                player.numOfPot += quantity
                print('\nHere you go!\n')
            else:
                print('you cannot hold that many!\n')
        else:
            print('you cannot afford that many!\n')
    else:
        clearScreen()
        print('No.\n')


def sell(player):
    clearScreen()
    notAvailable()      # Needs development
