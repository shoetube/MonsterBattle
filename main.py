#!/usr/bin/python3
# Above tells program where to find python3.

# IMPORTS
import FUNCTIONS


def main():
    FUNCTIONS.printTitle(FUNCTIONS.TITLE_STRING)
    player = FUNCTIONS.getPlayer()
    player.query()


main()
