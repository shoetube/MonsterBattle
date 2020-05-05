#!/usr/bin/python3
# Above tells program where to find python3.

# IMPORTS
import ITEMS
import ENEMIES
import LOCATIONS
import PLAYER
import FUNCTIONS


def main():
    FUNCTIONS.printTitle(FUNCTIONS.TITLE_STRING)
    player = FUNCTIONS.getPlayer()
    player.queryMove()


# Navigation and location functions
def plazaPrompt(player):
    clearScreen()
    print('You are standing in the plaza.\n')
    print('The ARENA is to the WEST.')
    print('The STORE is to the NORTH.')
    print('The LIBRARY, to the EAST.')
    print('To the SOUTH, there is a FOUNTAIN.\n')
    while True:     # Input checking
        iString = input('Where would you like to go?\n')
        iString = iString.lower()
        if iString == 'arena' or iString == 'west':
            arenaPrompt(player)
            break
        elif iString == 'store' or iString == 'north':
            storePrompt(player)
            break
        elif iString == 'library' or iString == 'east':
            libraryPrompt(player)
            break
        elif iString == 'fountain' or iString == 'south':
            fountainPrompt(player)
        pleaseEnter(['arena', 'store', 'library', 'fountain'])


# Arena - The player can battle enemies here to gain experience
def arenaPrompt(player):
    clearScreen()
    print('You are in the arena.\n')
    print('You can BATTLE or EXIT to the plaza.\n')
    while True:     # Input checking
        iString = whatToDo()
        if iString == 'battle':
            battle(player)
        elif iString == 'exit' or iString == 'plaza':
            plazaPrompt(player)
            break
        pleaseEnter(['battle', 'exit'])


def battle(player):
    clearScreen()
    enemy = getEnemy()
    print(f'{player.name} vs {enemy.name}!')
    battleRound = 1

    # WHILE - battle loop
    while player.alive and enemy.alive:
        print(f'\nRound {battleRound}')
        print(f'\nRemaining player health: {player.hp}/{player.maxHp}')
        print(f'Remaining enemy health: {enemy.hp}/{enemy.maxHp}')
        print('\nYou can ATTACK, HEAL, or SURRENDER.\n')
        iString = whatToDo()
        clearScreen()

        # ATTACK
        if iString == 'attack':
            player.attack(enemy)

        # HEAL
        elif iString == 'heal':
            # If player has no potions, continue to beginning of loop
            if player.numOfPot < 1:
                print("You don't have any potions left")
                continue
            else:   # ELSE use potion
                items.potion.use(player)
                print(f'You have {player.numOfPot} potions left')

        # SURRENDER
        elif iString == 'surrender':
            LOSE_EXP_SURRENDER = player.experience // 3
            print(f'If you surrender, you will lose ' +
                  f'{LOSE_EXP_SURRENDER} experience.\n')
            while True:
                choice = input('Are you sure that you want to surrender?\n')
                choice = choice.lower()
                if choice == 'yes':
                    oldExp = player.experience
                    player.experience -= LOSE_EXP_SURRENDER
                    print(f'\nYour experience points went from ' +
                          f'{oldExp} to {player.experience}.\n')
                    pressEnter()
                    arenaPrompt(player)
                elif choice == 'no':
                    clearScreen()
                    break
                else:
                    clearScreen()
                    pleaseEnter(['yes', 'no'])
                    continue
            continue
        else:
            continue

        # IF enemy alive, enemy attacks player
        if enemy.hp > 0:
            enemy.attack(player)

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
            player.experience += enemy.grantExp
            gainGold = enemy.dropGold()
            player.gold += gainGold
            print(f'\nYou gain {enemy.grantExp} experience.')
            print(f'You found {gainGold} pieces of gold.\n')
            pressEnter()
        battleRound += 1    # increment round number
    # END WHILE
    arenaPrompt(player)

# Store - buy and sell weapons and recovery items
def storePrompt(player):
    potionCost = 2
    clearScreen()
    print('You are in the store.\n')
    print('You can BUY, SELL, or EXIT to the plaza\n')

    while True:     # Input checking
        iString = whatToDo()

        # BUY
        if iString == 'buy':
            clearScreen()
            print('\nYou decide to buy.\n')
            print(f'You can buy potions for {potionCost} gold each\n')
            print(f'You currently have {player.numOfPot} potions.')
            print(f'You can have up to {MAX_POT} in your inventory\n')

            if player.numOfPot >= MAX_POT:
                print("You can't carry any more potions!\n")
                pressEnter()
                storePrompt(player)

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
                        pressEnter()
                        storePrompt(player)
                    else:
                        print('you cannot hold that many!\n')
                        pressEnter()
                        storePrompt(player)
                else:
                    print('you cannot afford that many!\n')
                    pressEnter()
                    storePrompt(player)
        elif iString == 'sell':
            clearScreen()
            print('\nYou decide to sell.')
            notAvailable()      # Needs development
            input('\n')
            pressEnter()
            storePrompt(player)
            break
        elif iString == 'exit' or iString == 'plaza':
            plazaPrompt(player)
            break
        else:
            pleaseEnter(['buy', 'sell', 'exit'])


# Library - Save or load character data and quit game. A utility area.
def libraryPrompt(player):
    clearScreen()
    print('You are in the library.\n')
    print('You can STUDY to level up.')
    print('You can SAVE or LOAD a character.')
    print('You can QUIT the game, or EXIT to the plaza\n')
    while True:     # Input checking
        iString = whatToDo()
        if iString == 'study':
            clearScreen()
            print('You decide to study\n')
            print(f'You currently have {player.experience} experience.')
            print(f'You need {player.levelUp()} experience to level up.\n')
            if player.experience >= player.levelUp():
                levelUp(player)
            else:
                print("You don't have enough experience yet.\n")
                pressEnter()
                libraryPrompt(player)
        elif iString == 'save':
            print('You have decided to save.')
            savePlayer(player)
            print('\nSave successful!\n')
        elif iString == 'load':
            print('You have decided to load.')
            player = loadPlayer()
            print('\nLoad successful!\n')
            print('Welcome, ' + player.name)
        elif iString == 'quit':
            print('\nYou have decided to quit the game.')
            sys.exit()
        elif iString == 'exit' or iString == 'plaza':
            plazaPrompt(player)
            break
        else:
            pleaseEnter(['save', 'load', 'quit', 'exit'])


def levelUp(player):
    print(f'You can increase your HP by {INC_HP_AMT}, your STRENGTH ' +
          f'by {INC_STR_AMT}, or you can CANCEL.\n')
    while True:
        iString = whatToDo()
        if iString == 'hp':
            oldHp = player.maxHp
            player.maxHp += INC_HP_AMT
            player.hp = player.maxHp
            player.experience -= player.levelUp()
            player.level += 1
            print(f'\nYour maximum HP went from {oldHp} to {player.maxHp}.')
            print(f'You are now level {player.level}!\n')
            pressEnter()
            break
        if iString == 'strength':
            oldStr = player.strength
            player.strength += INC_STR_AMT
            player.experience -= player.levelUp()
            player.hp = player.maxHp
            player.level += 1
            print(f'\nYour strength went from {oldStr} to {player.strength}.')
            print(f'You are now level {player.level}!\n')
            pressEnter()
            break
        elif iString == 'cancel':
            print('\nLevel up canceled.\n')
            pressEnter()
            break
        else:
            pleaseEnter(['hp', 'cancel'])
    libraryPrompt(player)


def fountainPrompt(player):     # Examine player character information
    clearScreen()
    print('You are at the fountain.\n')
    print('You can LOOK at your reflection,')
    print('you can DRINK from the fountain,')
    print('you can EXIT to the plaza.\n')
    while True:     # Input checking
        iString = whatToDo()
        if iString == 'look':
            clearScreen()
            print('\n')
            print('You look at your reflection in the water of the fountain\n')
            print(f'You are {player.name}, a {player.race} {player.job}.')
            print(f'You are currently level {player.level} with ' +
                  f'{player.experience} points of experience.')
            print(f'You are wielding a {player.weapon.name}.')
            print(f'You have {player.hp} of {player.maxHp} HP.')
            print(f'You have {player.strength} strength.')
            print(f'You are carrying {player.numOfPot} potions.')
            print(f'You have {player.gold} pieces of gold.\n')
            pressEnter()
            fountainPrompt(player)
            break
        elif iString == 'drink':
            clearScreen()
            print('\nYou drink from the fountain.')
            player.hp = player.maxHp
            print('Your HP is restored.\n')
            pressEnter()
            fountainPrompt(player)
            break
        elif iString == 'exit' or iString == 'plaza':
            plazaPrompt(player)
            break
        else:
            pleaseEnter(['look', 'drink', 'exit'])


main()
