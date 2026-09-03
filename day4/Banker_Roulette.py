from my_mod import random as rmod 

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
payer = rmod.randint(0, len(friends) - 1)
print(f"Looks like {friends[payer]} is paying for dinner for today")

payer_choice = rmod.choice(friends)
print(f"Looks like {payer_choice} is paying for dinner for next time ")


