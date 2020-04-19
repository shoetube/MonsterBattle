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

def createPlayer():
    name = input('What is your name?')
    player = Player(shortSword, 'human', 'knight', name)





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


