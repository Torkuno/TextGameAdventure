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


# The player
class Player(Entity):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)
        self.name = str(f"\033[0;34m{name}\033[0m")


# Enemies
class Enemy(Entity):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)


class Goblin(Enemy):
    def __init__(self):
        super().__init__(name="Goblin", hp=10, damage=5)


class Bat(Enemy):
    def __init__(self):
        super().__init__(name="Bat", hp=5, damage=3)


class Mimic(Enemy):
    def __init__(self):
        super().__init__(name="Mimic", hp=30, damage=5)


def battle(player, enemies):
    print(f"{player.name} faces off against {', '.join([enemy.name for enemy in enemies])}!")

    while player.is_alive() and any([enemy.is_alive() for enemy in enemies]):

        for enemy in enemies:
            if not enemy.is_alive():
                enemies.remove(enemy)

        print(f"\n{player.name} (\033[0;31m{player.hp} HP\033[0m)")
        for enemy in enemies:
            print(f"{enemy.name} (\033[0;31m{enemy.hp} HP\033[0m)")
        print()

        # Player's turn
        print("Actions:")
        action = input("[Attack, Block] >>> ")
        action = action.strip().lower()
        print()
        if action == "attack":
            target = choose_target(enemies)
            player.attack(target)
        elif action == "block":
            player.block()
        else:
            print("Invalid action!")
            continue

        # Enemies' turn
        for enemy in enemies:
            if enemy.is_alive():
                enemy.attack(player)

    if player.is_alive():
        print(f"{player.name} wins!")
    else:
        print("The enemies have defeated the player!")


def choose_target(enemies):
    print("Using numbers, choose your target:")
    for i, enemy in enumerate(enemies):
        print(f"[{i+1}] {enemy.name} (\033[0;31m{enemy.hp} HP\033[0m)")
    while True:
        choice = input()
        print()
        if choice.isdigit() and int(choice) <= len(enemies):
            return enemies[int(choice) - 1]
        else:
            print("Invalid choice. Please choose a valid target.")


if __name__ == "__main__":
    player = Player("Martin", 30, 5)
    enemy1 = Goblin()
    enemy2 = Bat()
    enemies = [enemy1, enemy2]

    battle(player, enemies)
