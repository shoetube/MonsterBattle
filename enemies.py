class enemy:
    def __init__(self, name, weapon, damage, hp):
        self.name = name
        self.weapon = weapon
        self.damage = damage
        self.hp = hp
        self.maxHp = hp
        self.alive = True


blueSlime = enemy('blue slime', 'sliminess', 2, 5)
