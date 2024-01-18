import random

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def attack_enemy(self, enemy):
        damage = max(0, self.attack - enemy.defense)
        enemy.take_damage(damage)
        return damage

class Player(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack=10, defense=5)
        self.experience = 0
        self.level = 1

    def level_up(self):
        self.level += 1
        self.health += 10
        self.attack += 5
        self.defense += 2
        print(f"Congratulations! You've reached level {self.level}.")

class Enemy(Character):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)

def create_enemy():
    enemies = [
        Enemy("Goblin", health=20, attack=8, defense=3),
        Enemy("Skeleton", health=15, attack=10, defense=2),
        Enemy("Orc", health=25, attack=12, defense=5),
    ]
    return random.choice(enemies)

def main():
    player_name = input("Enter your character's name: ")
    player = Player(player_name)

    print(f"Welcome, {player_name}! Let the adventure begin.")

    while player.is_alive():
        enemy = create_enemy()
        print(f"\nYou encounter a {enemy.name}!")

        while enemy.is_alive() and player.is_alive():
            print("\n1. Attack")
            print("2. Run")

            choice = input("Choose an action (1/2): ")

            if choice == "1":
                damage_dealt = player.attack_enemy(enemy)
                print(f"You dealt {damage_dealt} damage to the {enemy.name}.")

                if enemy.is_alive():
                    damage_taken = enemy.attack_enemy(player)
                    print(f"The {enemy.name} dealt {damage_taken} damage to you.")
            elif choice == "2":
                print("You run away from the battle.")
                break
            else:
                print("Invalid choice. Try again.")

        if player.is_alive():
            player.experience += 10
            print(f"\nYou defeated the {enemy.name} and gained 10 experience points.")

            if player.experience >= 50:
                player.level_up()

            print(f"\nCurrent stats - Level: {player.level}, Health: {player.health}, Experience: {player.experience}")

    print("\nGame over. Thanks for playing!")

if __name__ == "__main__":
    main()
