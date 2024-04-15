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
