import random
import math
import sys
import ITEMS

class Creature:
    def __init__(self, weapon, race, job):
        self.weapon = weapon    # Player weapon is a class object
        self.race = race        # String
        self.job = job          # String
        self.alive = True


class Player(Creature):     # Player class used for user character
    def __init__(self, weapon, race, job, name, location):
        super().__init__(weapon, race, job)
        self.name = name        # Player name. String.
        self.location = location
        self.hp = 10            # Current health points
        self.maxHp = 10         # Maximum health points
        self.strength = 1       # Increases damage dealt to enemy
        self.endurance = 1
        self.agility = 1
        self.dexterity = 1
        self.damage = self.strength + self.weapon.damage
        self.experience = 0     # Current experience points
        self.level = 1          # Current player level
        self.potion = ITEMS.potion
        self.numOfPot = 1
        self.gold = 0

    def attack(self, target):
            print(f'You attack the {target.name} ' +
                  f'with your {self.weapon.name}.')
            atkDmg = random.randint(0, self.damage)
            # Player attacks enemy
            if atkDmg > 0:  # 0 damage is treated as a miss
                print(f'You hit the {target.name}. ' +
                      f'The {target.name} loses {atkDmg} hp.')
                target.hp -= atkDmg
            else:
                print(f'You miss the {target.name}.')

    def levelUp(self):
        return math.floor((self.level**1.5)*5)

    def queryMove(self):
        self.location.welcome(self)
        print("'MOVE' on")
        while True:
            iString = input('Enter command: ')
            istring = iString.lower()
            if iString == 'quit' or iString == 'q':
                sys.exit()
            elif iString == 'help' or iString == 'h':
                self.helpMove()
            elif iString == 'location' or iString == 'l':
                self.location.welcome(self)
            elif iString == 'move' or iString == 'm':
                print('Move: off')
                self.queryContext()
            else:
                self.location.Move(self, iString)

    def queryContext(self):
        self.location.welcome(self)
        print("'MOVE' off")
        while True:
            iString = input('Enter command: ')
            istring = iString.lower()
            if iString == 'help' or iString == 'h':
                self.helpContext()
            elif iString == 'move' or iString == 'm':
                print('Move: on')
                self.queryMove()
            else:
                self.location.context(self, iString)

    def helpMove(self):
        print('''
UTILITY COMMANDS:
(Q)uit     - Quits the game
(H)elp     - reads this menu
(L)ocation - Repeats player location
(M)ode     - Toggles 'move' commands''')
        self.location.helpMove()

    def helpContext(self):
        print('''
UTILITY COMMANDS:
(H)elp     - reads this menu
(M)ode     - Toggles 'move' commands''')
        self.location.help()


class Enemy(Creature):  # Create complex enemies. (Not in use)
    def __init__(self, weapon, race, job):
        super().__init__(weapon, race, job)
        pass