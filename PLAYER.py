import random
import math
import sys
import FUNCTIONS
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

    def query(self):
        self.location.welcome(self)
        while True:
            iString = input('Enter command: ')
            istring = iString.lower()
            if iString == 'quit' or iString == 'q':
                self.confirmQuit()
            elif iString == 'help' or iString == 'h':
                self.helpMove()
            elif iString == 'location' or iString == 'l':
                self.location.welcome(self)
            elif iString == 'check' or iString == 'c':
                self.check()
            else:
                self.location.Move(self, iString)

    def confirmQuit(self):
        FUNCTIONS.clearScreen()
        s = input('Are you sure you want to quit?\n')
        s = s.lower()
        if s == 'yes' or s == 'y':
            sys.exit()
        else:
            self.query()

    def helpMove(self):
        FUNCTIONS.clearScreen()
        print('''
UTILITY COMMANDS:
(Q)uit     - Quits the game
(H)elp     - reads this menu
(L)ocation - Repeats player location
(C)heck    - check player stats
(M)ode     - Toggles 'move' commands''')
        self.location.helpMove()
        self.location.help()

    def check(self):
        print('\n'*40)
        print(f'''
Name:    {self.name}
race:    {self.race}
job:     {self.job}
HP:      {self.hp}/{self.maxHp}
str:     {self.strength}
level:   {self.level}
exp:     {self.experience}/{self.levelUp()}
gold:    {self.gold}
potions: {self.numOfPot}
weapon:  {self.weapon.name}
wpn dam: {self.weapon.damage}
''')


class Enemy(Creature):  # Create complex enemies. (Not in use)
    def __init__(self, weapon, race, job):
        super().__init__(weapon, race, job)
        pass
