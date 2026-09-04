class Weapon: 
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.weapon = None #Start with no weapon 

    def equid_weapon(self, new_weapon):
        self.weapon = new_weapon
        print(f"{self.name} equipped the {self.weapon.name}!")

    def attack(self, target):
        if self.weapon is not None:
            damage = self.weapon.damage
            print(f"{self.name} attack with {self.weapon.name} for {self.weapon.damage} damage!")
        else:
            damage = 1
            print(f"{self.name} punches for 1 damage!")
        target.take_damage(damage)
class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp 
        
    def roar(self):
        print(f"{self.name} roars angrily! ")

    def take_damage(self, amount):
        self.hp =max(0, self.hp - amount)
        print(f"{self.name} took {amount} damage! HP left: {self.hp}")
        if self.hp == 0:
            print(f"{self.name} has been defeated!")


class Goblin(Monster):
    def steal_gold(self):
        print(f"{self.name} stole 5 gold coins and scurried away!")

class Dragon(Monster):
    def breathe_fire(self):
        print(f"{self.name} breathes a torrent of fire! ")

#1. Create the separate objects 

g = Goblin("Grub", 20)
hero = Player("Aria", 100)
sword = Weapon("Iron Sword", 15)
bow = Weapon("Oak Bow", 8)

#Equip sword for more damage
hero.equid_weapon(sword)
print("\n--- Battle Starts! ---")
while g.hp > 0 and hero.hp > 0:
    hero.attack(g)

    if g.hp > 0:
        #If the goblin survived, it retaliates (dealing 4 damage)
        print(f"{g.name} counter-attacks!")
        hero.hp = max(0, hero.hp - 4)
        print(f"{hero.name} has {hero.hp} HP left \n")

print("Battle ended.") 

