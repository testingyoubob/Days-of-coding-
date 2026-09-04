from entities import Character, Weapon, Potion, Enemy

# Setup the encounter 
hero = Character(name="Aria", hp=50)
sword = Weapon(name="Rusty Broadsword", damage=10)
hero.equip(sword)  # Changed 'equid' to 'equip'

healing_potion = Potion(name="Health Potion", heal_amount=20)
goblin = Enemy(name="Dungeon Goblin", hp=25, raw_damage=6)

print("--- Battle Encounter ---")
print(f"A wild {goblin.name} blocks your path!\n")

# Battle loop: Runs as long as both fighters are alive 
while hero.hp > 0 and goblin.hp > 0:
    print(f"\nYour HP: {hero.hp}/{hero.max_hp} | {goblin.name} HP: {goblin.hp}/{goblin.max_hp}")
    print("Action: [1] Attack  [2] Drink Potion")
    choice = input("> ")

    # Player Turn 
    if choice == "1":
        hero.attack(goblin)
    elif choice == "2":
        if healing_potion is not None:
            healing_potion.use(hero)
            healing_potion = None  # Consumed!
        else: 
            print("You don't have any potions left!")
            continue
    else: 
        print("Invalid action! Choose 1 or 2.")
        continue

    # Enemy Turn (Only if still standing)
    if goblin.hp > 0:
        goblin.attack(hero)

# UNINDENTED: Only runs once someone reaches 0 HP
print("\n--- Battle Concluded ---")
if hero.hp > 0:
    print(f"Victory! {hero.name} defeated the {goblin.name}!")
else: 
    print(f"Defeat... {hero.name} was bested in combat by {goblin.name}.")