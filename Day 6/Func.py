def full_name(first, middle, last, display):
    name = first + " " + middle + " " + last 
    if display:
        print(name)
    return name 

full_name("Rob", "W", "Oliver", True)
compete_name = full_name("Rob", "W", "Oliver", display=False)
print(compete_name)