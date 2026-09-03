from my_mod import random as rmod
from my_mod import game_text_image as gti 


user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors \n : "))
computer_choice = rmod.randint(0, 2)

if user_choice >= 0 and user_choice <= 2:
    print(gti[user_choice])
    print(f"{gti[computer_choice]}")
    print(f"Computer chose")

if user_choice >=3 or user_choice < 0: 
    print(f"{gti[3]}")
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    
    print("You lose!")
elif computer_choice > user_choice: 
    
    print("You lose!")
elif user_choice > computer_choice:
    
    print("You win!")
elif computer_choice == user_choice:
    
    print("Draw!")
