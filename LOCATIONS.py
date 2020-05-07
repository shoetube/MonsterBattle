# player.query() only runs after title screen and character creation
# or load

import sys
import FUNCTIONS


class Location:
    def __init__(self, name='location', north=None,
                 east=None,
                 south=None, west=None):
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.name = name

    def welcome(self, player):
        FUNCTIONS.clearScreen()
        if self.north is not None:
            print(f'To the north is the {self.north.name}.')
        if self.east is not None:
            print(f'To the east is the {self.east.name}.')
        if self.south is not None:
            print(f'To the south is the {self.south.name}.')
        if self.west is not None:
            print(f'To the west is the {self.west.name}.')
        print(f'\nYou are at the {self.name}\n')
        self.options()

    def options(self):
        pass

    def helpMove(self):
        print('''
MOVE COMMANDS:
(N)orth - Moves player to the north.
(E)ast  - Moves player to the east.
(S)outh - Moves player to the south.
(W)est  - Moves player to the west.''')

    def Move(self, player, iString):

        if iString == 'north' or iString == 'n':
            if self.north is not None:
                player.location = self.north
                player.query()
            else:
                self.invalidDirection()
        elif iString == 'east' or iString == 'e':
            if self.east is not None:
                player.location = self.east
                player.query()
            else:
                self.invalidDirection()
        elif iString == 'south' or iString == 's':
            if self.south is not None:
                player.location = self.south
                player.query()
            else:
                self.invalidDirection()
        elif iString == 'west' or iString == 'w':
            if self.west is not None:
                player.location = self.west
                player.query()
            else:
                self.invalidDirection()
        else:
            self.context(player, iString)

    def help(self):
        pass

    def context(self, player, iString):
        self.invalid()

    def invalidDirection(self):
        FUNCTIONS.clearScreen()
        print("\nCan't go that way.")

    def invalid(self):
        FUNCTIONS.clearScreen()
        print("INVALID COMMAND. Try entering 'help'.")


class Plaza(Location):
    def __init__(self, name='location', north=None,
                 east=None, south=None, west=None):
        super().__init__(name, north, east, south, west)


class Store(Location):
    def __init__(self, name='location', north=None,
                 east=None, south=None, west=None):
        super().__init__(name, north, east, south, west)

    def options(self):
        (print(f'Here you can buy or sell.\n'))

    def context(self, player, iString):
        if iString == 'buy':
            FUNCTIONS.buy(player)
        elif iString == 'sell':
            FUNCTIONS.sell(player)
        else:
            self.invalid()

    def help(self):
        print('''
STORE COMMANDS:
buy  - Purchase items from the store.
sell - Exchange unwanted items for gold.''')


class Library(Location):
    def __init__(self, name='location', north=None,
                 east=None, south=None, west=None):
        super().__init__(name, north, east, south, west)

    def options(self):
        (print(f'Here you can save, load, or study.\n'))


    def context(self, player, iString):
        if iString == 'save':
            FUNCTIONS.clearScreen()
            FUNCTIONS.savePlayer(player)
            print('\nSave successful!\n')
        elif iString == 'load':
            FUNCTIONS.clearScreen()
            player = FUNCTIONS.loadPlayer()
            print('\nLoad successful!\n')
            print('Welcome, ' + player.name)
        elif iString == 'study':
            FUNCTIONS.clearScreen()
            print(f'You currently have {player.experience} ' +
                  f'experience.')
            print(f'You need {player.levelUp()} experience to ' +
                  f'level up.\n')
            if player.experience >= player.levelUp():
                FUNCTIONS.levelUp(player)
            else:
                print("You don't have enough experience yet.\n")
#                FUNCTIONS.pressEnter()
#                player.query()
        else:
            self.invalid()

    def help(self):
        print('''
LIBRARY COMMANDS:
save  - Save character data.
load - Load saved character data.
study - Spend experience points to increase player stats.''')


class Fountain(Location):
    def __init__(self, name='location', north=None,
                 east=None, south=None, west=None):
        super().__init__(name, north, east, south, west)

    def options(self):
        (print(f'Here you can drink.\n'))

    def context(self, player, iString):
        if iString == 'drink':
            FUNCTIONS.clearScreen()
            print('\nYou drink from the fountain.')
            player.hp = player.maxHp
            print('Your HP is restored.\n')
        else:
            self.invalid()

    def help(self):
        print('''
FOUNTAIN COMMANDS:
drink - Drink from the fountain to restore HP.''')


class Arena(Location):
    def __init__(self, name='location', north=None,
                 east=None, south=None, west=None):
        super().__init__(name, north, east, south, west)

    def options(self):
        (print(f'Here you can battle.\n'))

    def context(self, player, iString):
        if iString == 'battle':
            FUNCTIONS.battle(player)
        else:
            self.invalid()

    def help(self):
        print('''
ARENA COMMANDS:
battle - Battle enemies to gain gold and experience.''')


plaza = Plaza(name='plaza')
store = Store(name='store', south=plaza)
arena = Arena(name='arena', east=plaza)
library = Library(name='library', west=plaza)
fountain = Fountain(name='fountain', north=plaza)
plaza.north = store
plaza.east = library
plaza.south = fountain
plaza.west = arena
