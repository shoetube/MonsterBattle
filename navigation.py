#!/usr/bin/python3 
import sys
import pickle
class Creature:
    def __init__(self, weapon, race, job):
        self.weapon = weapon
        self.race   = race
        self.job    = job
        self.alive  = True

class Player(Creature):
    def __init__(self, weapon, race, job, name):
        super().__init__(weapon, race, job)
        self.name       = name
        self.weapon     = weapon
        self.hp         = 10
        self.maxHp      = 10
        self.experience = 0
        self.level      = 1

class Enemy(Creature):
    def __init__(self, weapon, race, job):
        super().__init__(weapon, race, job)
        pass
        
class weapon:
    def __init__(self, family, name, damage, value):
        self.family = family
        self.name   = name
        self.damage = damage
        self.value  = value

# Navigation functions
def plazaPrompt(player):
    clearScreen()
    print('You are standing in the plaza.')
    print('You can go to the arena, the store, or the archives. Or you can check your reflection in the fountain')
    while True:
        iString = input('Where would you like to go?\n')
        if iString == 'arena':
            print('You go to the arena.')
            arenaPrompt(player)
            break
        elif iString == 'store':
            print('You go to the store.')
            storePrompt(player)
            break
        elif iString == 'archives':
            print('You go to the archives')
            archivesPrompt(player)
            break
        elif iString == 'check':
            whoAmI(player)
        print("please enter 'arena', 'store', or 'archives'")

def arenaPrompt(player):
    clearScreen()
    print('You are in the arena.')
    print('You can battle or return.')
    while True:
        iString = input('What would you like to do?\n')
        if iString == 'battle':
            print('You have decided to battle.')
            notAvailable()  # Needs development
        elif iString == 'return':
            print('You have decided to go to return to the plaza.')
            plazaPrompt(player)
            break
        print("Please enter 'battle' or 'return'")

def storePrompt():
    clearScreen()
    print('You are in the store.')
    print('You can buy, sell, or return')
    while True:
        iString = input('What would you like to do?\n')
        if iString == 'buy':
            print('You decide to buy.')
            notAvailable()  # Needs development
        elif iString == 'sell':
            print('You decide to sell.')
            notAvailable()  # Needs development
        elif iString == 'return':
            print('You have decided to return to the plaza.')
            plazaPrompt(player)
            break
        print("Please enter 'buy', 'sell', or 'return'.")

def archivesPrompt(player):
    clearScreen()
    print('You are in the archives.')
    print('You can save, load, quit, or return')
    while True:
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
        elif iString == 'return':
            print('You have decided to return to the plaza.')
            plazaPrompt(player)
            break
        print("please enter 'save', 'load', 'quit', or 'return'.")

def whoAmI(player):
    print(f'You are {player.name}. A {player.race} {player.job} wielding a {player.weapon.name}.')

# Place holder for undeveloped features
def notAvailable():
    print('\nThat feature is not available yet.\n')

# Fills screen with blank lines
def clearScreen():
    print('\n'*40)



# Predetermined weapon choices
dagger     = weapon('sword', 'dagger'      , 2, 1)
shortSword = weapon('sword', 'short sword' , 3, 1)
longSword  = weapon('sword', 'long sword'  , 4, 1)

bigStick   = weapon('club' , 'big stick'   , 2, 1)
nailBat    = weapon('club' , 'nail bat'    , 3, 1)
mace       = weapon('club' , 'mace'        , 4, 1)

sharpStick = weapon('spear', 'sharp stick' , 2, 1)
woodenSpear= weapon('spear', 'wooden spear', 3, 1)
halberd    = weapon('spear', 'halberd'     , 4, 1)

# Begin game
clearScreen()
print('Welcome to Monster Battle!')
input('Press ENTER to continue')
clearScreen()
choice = input('Would you like to create a character or load?\n')
if choice == 'create':
    name = input('What is your name?\n')
    player = Player(shortSword, 'human', 'knight', name)
elif choice == 'load':
    iFile = open('savePlayer.pickle', 'rb')
    player = pickle.load(iFile)
    iFile.close()
plazaPrompt(player) 
