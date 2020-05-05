from random import randint
from random import choice
class enemy:
    def __init__(self, name, weapon, damage, hp, grantExp, goldSeed):
        self.name = name
        self.weapon = weapon
        self.damage = damage
        self.hp = hp
        self.maxHp = hp
        self.alive = True
        self.grantExp = grantExp
        self.goldSeed = goldSeed

    def dropGold(self):
        return randint(0, self.goldSeed)

    def attack(self, target):
        print(f'The {self.name} attacks you with its {self.weapon}.')
        atkDmg = randint(0, self.damage)
        # Enemy attacks player
        if atkDmg > 0:
            print(f'The {self.name} hits you. You lose {atkDmg} hp.')
            target.hp -= atkDmg
        else:
            print(f'The {self.name} misses you.')

# PARAMETERS = name, weapon, damage, hp, granthp, goldSeed
BLUE_SLIME = enemy('blue slime', 'sliminess', 2, 5, 1, 2)
SMALL_RAT = enemy('small rat', 'bite', 2, 3, 1, 1)
SKELETAL_HAND = enemy('skeletal hand', 'flick', 3, 5, 2, 2)
RED_SLIME = enemy('red slime', 'hot slime', 4, 10, 3, 3)

enemyList = [
    BLUE_SLIME,
    SMALL_RAT,
    SKELETAL_HAND,
    RED_SLIME,
]


