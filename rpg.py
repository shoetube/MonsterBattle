#!/usr/bin/python3
#This program creates a player and a monster to battle to the death interactively.

#Imports randInt. Used for damage calculations.
from random import randint

#Call to create a player character
class createPlayer:
    def __init__(self, name, weapon, damage, hp):
        self.name   = name
        self.weapon = weapon
        self.damage = damage
        self.hp     = hp
        self.maxHp  = hp
        self.alive  = True

    def attack(self, target):
        print(f'\nYou attack the {target.name} with your {self.weapon}.')
        atkDmg = randint(0,self.damage)
        if atkDmg > 0:
            print(f'You hit the {target.name}. The {target.name} loses {atkDmg} hp.')
            target.hp -= atkDmg
        else:
            print(f'You miss the {target.name}.')

        if target.hp > 0:
            target.attack(self)
        else:
            print(f'You have slain the {target.name}.') 
            target.alive = False

#Call to create a monster
class createMonster:
    def __init__(self, race, job, weapon, damage, hp):
        self.name   = race + ' ' + job
        self.weapon = weapon
        self.damage = damage
        self.hp     = hp
        self.maxHp  = hp
        self.alive  = True

    def attack(self, target):
        print(f'\nThe {self.name} attacks you with its {self.weapon}.')
        atkDmg = randint(0,self.damage)
        if atkDmg > 0:
            print(f'The {self.name} hits you. You lose {atkDmg} hp.')
            target.hp -= atkDmg
        else:
            print(f'The {self.name} misses you.')
        if target.hp <= 0:
            print(f'You have been slain by the {self.name}.')
            target.alive = False

#Create instance of a player
player  = createPlayer ('Scott',           'sword',  4, 10)

#Monster generator
def generateMonster():
    monAttributes = {'race': ['goblin', 'elf', 'orc'], 'job' : ['scout', 'warrior', 'berserker'], 'weapon' : ['club', 'axe', 'sword', 'spear']}
    raceLength   = monAttributes['race'].__len__() - 1
    jobLength    = monAttributes['job'].__len__() - 1
    weaponLength = monAttributes['weapon'].__len__() - 1
    monRace   = monAttributes['race'][randint(0, raceLength)]
    monJob    = monAttributes['job'][randint(0, jobLength)]
    monWeapon = monAttributes['weapon'][randint(0,weaponLength)]
    return createMonster(monRace, monJob, monWeapon, 4, 10)

monster = generateMonster()    

#Welcome screen
print('\n'*30)
print('Welcome to Monster Battle!')

battleRound = 1

#Runs game until one combatant dies then exits
while player.alive and monster.alive:
    print(f'\nRemaining player health: {player.hp}')
    print(f'Remaining monster health: {monster.hp}')
    inString=input('\nPress ENTER to attack: ')
    if inString == '':

        #clears screen after first run
        print('\n'*30)
        print(f'Round {battleRound}')
        battleRound += 1

        #engage first round of attacks
        player.attack(monster)
    else:
        print('Command not recognized')
print('\nGame over.')
