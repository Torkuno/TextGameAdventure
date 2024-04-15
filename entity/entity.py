class Entity:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.is_blocking = False

    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.damage} damage!")
        target.take_damage(self.damage)
        if not target.is_alive():
            print(f"{target.name} has been defeated!")

    def block(self):
        self.is_blocking = True
        print(f"{self.name} is blocking!")

    def take_damage(self, damage):
        if self.is_blocking:
            damage = max(1, damage // 2)  # blocking reduces damage by 50%
            self.is_blocking = False
            print(f"{self.name} blocks, reducing damage to {damage}.")
            self.hp -= damage
        else:
            self.hp -= damage
            if self.hp < 0:
                self.hp = 0

    def is_alive(self):
        return self.hp > 0