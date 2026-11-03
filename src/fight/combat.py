from random import randint


class Fighter:
    """This class represents a generic fighter character."""

    def __init__(self, name, health, defense, power, damage):
        """Initialize the fighter with the given attributes."""
        self.name = name
        self.health = health
        self.defense = defense
        self.power = power
        self.damage = damage


    def alive(self):
        """Determine if the fighters are alive."""

        return self.health > 0


    def attack(self, opponent):
        """Have the fighter attack an opponent."""

        roll = randint(1, 20)
        if roll + self.power - opponent.defense > 12:
            print(f"{self.name} hits {opponent.name} for {self.damage} points")
            opponent.wound(self.damage)
            if not opponent.alive():
                print(f"{self.name} won!")
        else:
            print(f"{self.name} missed.")


    def wound(self, amount):
        """Apply damage to the fighter."""

        self.health -= amount
        if not self.alive():
            print(f"{self.name} died.")


    def print_status(self):
        """Print the current status of the fighter."""
        print(f"{self.name} has {self.health} health.")


f1 = Fighter(name="Annie", health=10, defense=4, power=5, damage=3)
f2 = Fighter(name="Paul", health=11, defense=5, power=4, damage=2)
f3 = Fighter(name="Mary", health=15, defense=5, power=7, damage=8)
f4 = Fighter(name="EB", health=20, defense=10, power=2, damage=2)

print(f"{f1.name} vs {f2.name} vs {f3.name} vs {f4.name}")
round = 1

while f1.alive() and f2.alive() and f3.alive() and f4.alive():
    print(f"\nRound {round}")
    f1.print_status()
    f2.print_status()
    f3.print_status()
    f4.print_status()
    answer = input(f"Should {f1.name} attack? (2 or 3 or 4) ")
    if answer.lower() == "2":
        f1.attack(f2)
    if answer.lower() == "3":
        f1.attack(f3)
    if answer.lower() == "4":
        f1.attack(f4)
    if f2.alive():
        answer = input(f"Should {f2.name} attack? (1 or 3 or 4) ")
        if answer.lower() == "1":
            f2.attack(f1)
        if answer.lower() == "3":
            f2.attack(f3)
        if answer.lower() == "4":
            f2.attack(f4)
    if f3.alive():
        answer = input(f"Should {f3.name} attack? (1 or 2 or 4) ")
        if answer.lower() == "1":
            f3.attack(f1)
        if answer.lower() == "2":
            f3.attack(f2)
        if answer.lower() == "4":
            f3.attack(f4)
    if f4.alive():
        answer = input(f"Should {f4.name} attack? (1 or 2 or 3) ")
        if answer.lower() == "1":
            f4.attack(f1)
        if answer.lower() == "2":
            f4.attack(f2)
        if answer.lower() == "3":
            f4.attack(f3)
    round += 1

print("Fight over.")
