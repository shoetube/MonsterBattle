#!/usr/bin/python3

from random import randint, choice

class Weapon:
    def __init__(self, name, damage, accuracy):
        self.name = name
        self.damage = damage
        self.accuracy = accuracy

class Creature:
    def __init__(self, name, weapon, hp):
        self.name = name
        self.weapon = weapon
        self.hp = hp
        self.maxHp = hp
        self.alive = True

class Player(Creature):
    pass

class Enemy(Creature):
    pass


# takes accuracy (int) as a parameter and returns wether a hit was a success or not as a boolean
def isHit(accuracy):
    if (accuracy - randint(0,100) > 0):
        return True
    else:
        return False


spear = Weapon('spear', 2, 95)
club  = Weapon('club',  3, 65)
axe   = Weapon('axe',   4, 45)
weaponList = [spear, club, axe]
randomWeapon = choice(weaponList)

# This code is designed to show the damage per round of each weapon
weapons = [spear, club, axe]
for i in weapons:
    rounds = 0
    totDam = 0
    hp = 1000
    while hp > 0:
        if isHit(i.accuracy):
            hp -= i.damage
            totDam += i.damage
        rounds += 1
    print(f'DPR: {totDam/rounds}') 
    print(f'{i.name} rounds: {rounds}')
    

