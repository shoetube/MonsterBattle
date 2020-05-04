#!/usr/bin/python3


# player.query() only runs after title screen and character creation or load

import sys


def clearScreen():
    print('\n'*40)


class Location:
    def __init__(self, name='location', north=None, east=None,
                 south=None, west=None):
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.name = name

    def welcome(self, player):
        clearScreen()
        print(f'\nYou are at the {self.name}')

    def help(self, player):
        print('''
CONTEXT SPECIFIC COMMANDS:
(N)orth - Moves player to the north
(E)ast  - Moves player to the east
(S)outh - Moves player to the south
(W)est  - Moves player to the west''')

    def Navigation(self, player, iString):
        if iString == 'north' or iString == 'n':
            if self.north is not None:
                print('Going north')
                player.location = self.north
                player.query()
            else:
                clearScreen()
                print("\nCan't go that way.")
        elif iString == 'east' or iString == 'e':
            if self.east is not None:
                print('Going east')
                player.location = self.east
                player.query()
            else:
                clearScreen()
                print("\nCan't go that way.")
        elif iString == 'south' or iString == 's':
            if self.south is not None:
                print('Going south')
                player.location = self.south
                player.query()
            else:
                clearScreen()
                print("\nCan't go that way.")
        elif iString == 'west' or iString == 'w':
            if self.west is not None:
                print('going west')
                player.location = self.west
                player.query()
            else:
                clearScreen()
                print("\nCan't go that way.")
        else:
            clearScreen()
            print('\nEnter NORTH, EAST, SOUTH, or WEST.')


class Plaza(Location):
    def __init__(self, name='location', north=None, east=None, south=None,
                 west=None):
        super().__init__(name, north, east, south, west)


class Store(Location):
    def __init__(self, name='location', north=None, east=None, south=None,
                 west=None):
        super().__init__(name, north, east, south, west)


class Library(Location):
    def __init__(self, name='location', north=None, east=None, south=None,
                 west=None):
        super().__init__(name, north, east, south, west)


class Fountain(Location):
    def __init__(self, name='location', north=None, east=None, south=None,
                 west=None):
        super().__init__(name, north, east, south, west)


class Arena(Location):
    def __init__(self, name='location', north=None, east=None, south=None,
                 west=None):
        super().__init__(name, north, east, south, west)


plaza = Plaza(name='plaza')
store = Store(name='store', south=plaza)
arena = Arena(name='arena', east=plaza)
library = Library(name='library', west=plaza)
fountain = Fountain(name='fountain', north=plaza)
plaza.north = store
plaza.east = library
plaza.south = fountain
plaza.west = arena


class Player:
    def __init__(self, location):
        self.location = location

    def query(self):
        self.location.welcome(self)
        print("Enter 'help' for command descriptions")
        while True:
            iString = input('Enter command: ')
            istring = iString.lower()
            if iString == 'quit' or iString == 'q':
                sys.exit()
            elif iString == 'help' or iString == 'h':
                self.help()
            elif iString == 'location' or iString == 'l':
                self.location.welcome(self)
            else:
                self.location.Navigation(self, iString)

    def help(self):
        print('''
ANY TIME COMMANDS:
(Q)uit     - Quits the game
(H)elp     - reads this menu
(L)ocation - Repeats player location''')

        self.location.help(self)


player = Player(plaza)

player.query()
