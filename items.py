##############################################################################
# Items is a module used to store the various items that Monster Battle uses #
##############################################################################

class weapon: # Create weapons used player and some enemies
    def __init__(self, family, name, damage, value):
        self.family = family # This is category of weapon
        self.name   = name   # More specific weapon name
        self.damage = damage # Base damage of weapon
        self.value  = value  # Base value of weapon. Used for buying and selling

# Predetermined weapon choices
dagger     = weapon('sword', 'dagger'      , 2, 1)
shortSword = weapon('sword', 'short sword' , 3, 2)
longSword  = weapon('sword', 'long sword'  , 4, 3)

bigStick   = weapon('club' , 'big stick'   , 2, 1)
nailBat    = weapon('club' , 'nail bat'    , 3, 2)
mace       = weapon('club' , 'mace'        , 4, 3)

sharpStick = weapon('spear', 'sharp stick' , 2, 1)
woodenSpear= weapon('spear', 'wooden spear', 3, 2)
halberd    = weapon('spear', 'halberd'     , 4, 3)
