#!/usr/bin/python3 
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
def plazaPrompt():
    clearScreen()
    print('You are standing in the plaza.')
    print('You can go to the arena, the store, or the archives.')
    while True:
        iString = input('Where would you like to go?\n')
        if iString == 'arena':
            print('You go to the arena.')
            arenaPrompt()
            break
        elif iString == 'store':
            print('You go to the store.')
            storePrompt()
            break
        elif iString == 'archives':
            print('You go to the archives')
            archivesPrompt()
            break
        print("please enter 'arena', 'store', or 'archives'")

def arenaPrompt():
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
            plazaPrompt()
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
            plazaPrompt()
            break
        print("Please enter 'buy', 'sell', or 'return'.")

def archivesPrompt():
    clearScreen()
    print('You are in the archives.')
    print('You can save, load, quit, or return')
    while True:
        iString = input('What would you like to do?\n')
        if iString == 'save':
            print('You have decided to save.')
            notAvailable()  # Needs development
        elif iString == 'load':
            print('You have decided to load.')
            notAvailable()  # Needs development
        elif iString == 'quit':
            print('You have decided to quit the game.')
            break
        elif iString == 'return':
            print('You have decided to return to the plaza.')
            plazaPrompt()
            break
        print("please enter 'save', 'load', 'quit', or 'return'.")

# Place holder for undeveloped features
def notAvailable():
    print('\nThat feature is not available yet.\n')

# Fills screen with blank lines
def clearScreen():
    print('\n'*40)

# Character creation
def createPlayer():
    clearScreen()
    name = input('What is your name?\n')
    player = Player(shortSword, 'human', 'knight', name)
    plazaPrompt() 

# Welcome screen. 
def splash():
    clearScreen()
    print('Welcome to Monster Battle!')
    input('Press ENTER to continue')
    createPlayer()

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

# Runs game
splash()
