from random import seed 
from random import randint 

number = randint(1, 10)
loopy = True

while loopy:
    try: 
        your_number = int(input("Guess between 1-10 "))
        if number != your_number:
            print("Sorry that's not the right number")
        elif number == your_number:
            print("You guess it right")
        elif your_number > 10 or your_number < 0: 
            print("Try a number lower that 10 or higher that 0")
        else:
            print("Try again")
        again = input("Do you want to play again? y/n ")
        if again == "y":
            continue
        elif again == "n":
            loopy = False
        else:
            print("Needs to be a y for yes or n for no \n ending program")
            break
    except ValueError:
        print("Error wasn't the correct output, numbers only")
    
