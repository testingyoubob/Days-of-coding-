class Weapon: 
    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage

class Potion: 
    def __init__(self, name: str, heal_amount: int): 
        self.name = name
        self.heal_amount = heal_amount

    def use(self, target):
        target.hp = min(target.max_hp, target.hp + self.heal_amount)
        print(f"{target.name} drank {self.name} and healed! HP {target.hp}/{target.max_hp}")

class Character: 
    def __init__(self, name: str, hp: int): 
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.weapon = None 

    def equip(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} equipped the {weapon.name}")

    def take_damage(self, amount: int): 
        self.hp = max(0, self.hp - amount)
        print(f"{self.name} take {amount} damage! ({self.hp}/{self.max_hp} HP)")

    def attack(self, target):
        damage = self.weapon.damage if self.weapon else 2 
        weapon_name = self.weapon.name if self.weapon else "bare firsts"
        print(f"{self.name} attack {target.name} with {weapon_name} for {damage} damage!")
        target.take_damage(damage)

class Enemy(Character): 
    def __init__(self, name: str, hp: int, raw_damage: int):
        super().__init__(name, hp)
        self.raw_damage = raw_damage 

    #Enemies don't need equipped weapon becaue they will attack with raw_damage
    def attack(self, target):
        print(f"{self.name} strikes {target.name} for {self.raw_damage} damage!")
        target.take_damage(self.raw_damage)   