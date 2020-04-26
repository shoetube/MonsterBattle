from random import randint
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


blueSlime = enemy('blue slime', 'sliminess', 2, 5, 1, 2)
