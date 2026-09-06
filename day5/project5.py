import random as rand 
#Create the numbers, letters, and symbols used in this project. 
numbers = list("0123456789")
letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
symbols = list("!@#$%^&*()_+-=[]{}|;':\",./<>?")  

#Get user number input for all characters 
print("Welome to the password generator")
nr_letters = int(input("How many letter would you like in your password?\n "))
nr_symbols = int(input("How many symbols would you like? \n "))
nr_number = int(input("How many numbers would you like? \n "))

#Take user input numbers for each character type and randomly pick out our characters. 
password = ""
for char in range(1, nr_letters + 1):
    random_char = rand.choice(letters)
    password += random_char
for char in range(1, nr_symbols + 1):
    random_char = rand.choice(symbols)
    password += random_char
for char in range(1, nr_letters + 1):
    random_char = rand.choice(numbers)
    password += random_char

#Turn our password into a list so it can be shuffled 
print(password)
password = list(password)


rand.shuffle(password)
final_password ="".join(password)
#Final password, totally mix up. 
print(final_password)





