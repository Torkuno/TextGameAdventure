from .entity import Entity


class Enemy(Entity):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)

class Goblin(Enemy):
    def __init__(self):
        super().__init__(name="Goblin", hp=10, damage=5)


class Bat(Enemy):
    def __init__(self):
        super().__init__(name="Bat", hp=5, damage=3)


class AlphaHound(Enemy):
    def __init__(self):
        super().__init__(name="Alpha Hound", hp=15, damage=5)


class Mimic(Enemy):
    def __init__(self):
        super().__init__(name="Mimic", hp=30, damage=5)
