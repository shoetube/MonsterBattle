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


main()
