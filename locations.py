# player.queryMove() only runs after title screen and character creation
# or load

import sys


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
        clearScreen()
        print(f'\nYou are at the {self.name}')

    def helpMove(self):
        print('''
MOVE COMMANDS:
(N)orth - Moves player to the north.
(E)ast  - Moves player to the east.
(S)outh - Moves player to the south.
(W)est  - Moves player to the west.
(M)ove  - Toggle move''')

    def Move(self, player, iString):

        if iString == 'north' or iString == 'n':

            if self.north is not None:
                print('Going north')
                player.location = self.north
                player.queryMove()

            else:
                invalidDirection()

        elif iString == 'east' or iString == 'e':

            if self.east is not None:
                print('Going east')
                player.location = self.east
                player.queryMove()

            else:
                invalidDirection()

        elif iString == 'south' or iString == 's':

            if self.south is not None:
                print('Going south')
                player.location = self.south
                player.queryMove()

            else:
                invalidDirection()

        elif iString == 'west' or iString == 'w':

            if self.west is not None:
                print('going west')
                player.location = self.west
                player.queryMove()

            else:
                invalidDirection()

        else:
            invalid()

    def help(self):
        pass

    def context(self, player, iString):
        pass

    def invalidDirection(self):
        clearScreen()
        print("\nCan't go that way.")


    def invalid(self):
        clearScreen()
        print("INVALID COMMAND. Try entering 'help'.")

class Plaza(Location):
    def __init__(self, name='location', north=None,
                 east=None, south=None, west=None):
        super().__init__(name, north, east, south, west)


class Store(Location):
    def __init__(self, name='location', north=None,
                 east=None, south=None, west=None):
        super().__init__(name, north, east, south, west)

    def help(self):
        print('''
STORE COMMANDS:
buy  - Purchase items from the store.
sell - Exchange unwanted items for gold.''')

class Library(Location):
    def __init__(self, name='location', north=None,
                 east=None, south=None, west=None):
        super().__init__(name, north, east, south, west)

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

    def context(self, player, iString):
        if iString == 'drink':
            print('You entered drink.')
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

    def help(self):
        print('''
ARENA COMMANDS:
battle - Battle enemies to gain gold and experience.''')

def clearScreen():
    print('\n'*40)


plaza = Plaza(name='plaza')
store = Store(name='store', south=plaza)
arena = Arena(name='arena', east=plaza)
library = Library(name='library', west=plaza)
fountain = Fountain(name='fountain', north=plaza)
plaza.north = store
plaza.east = library
plaza.south = fountain
plaza.west = arena
