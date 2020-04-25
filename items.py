##############################################################################
# Items is a module used to store the various items that Monster Battle uses #
##############################################################################


class weapon:   # Create weapons used by player and some enemies
    def __init__(self, family, name, damage, value):
        self.family = family    # This is category of weapon
        self.name = name        # More specific weapon name
        self.damage = damage    # Base damage of weapon
        self.value = value      # Base value of weapon


# Predetermined weapon choices
dagger = weapon('sword', 'dagger', 2, 1)
shortSword = weapon('sword', 'short sword', 3, 2)
longSword = weapon('sword', 'long sword', 4, 3)

bigStick = weapon('club', 'big stick', 2, 1)
nailBat = weapon('club', 'nail bat', 3, 2)
mace = weapon('club', 'mace', 4, 3)

sharpStick = weapon('spear', 'sharp stick', 2, 1)
woodenSpear = weapon('spear', 'wooden spear', 3, 2)
halberd = weapon('spear', 'halberd', 4, 3)


# restores about 1/3 of player's health untested. should probably change
# to floor or ceiling
class potion:
    def __init__():
        pass

    def use(target):
        oldHp = target.hp
        target.numOfPot -= 1
        healAmt = target.maxHp // 3
        target.hp += healAmt
        if target.hp > target.maxHp:
            target.hp = target.maxHp
        newHp = target.hp
        print(f'You gain {newHp-oldHp} hp!')
