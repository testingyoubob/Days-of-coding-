#Creates the class
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
#Methods change data in the Class. 
    def sharpen(self, bonus):
        self.damage += bonus 
        print(f" {self.name} was sharpon! Damage is now {self.damage}")


#Create a weapon 
sword = Weapon("Iron Sword", 10)
#Use Medthod 
sword.sharpen(5)