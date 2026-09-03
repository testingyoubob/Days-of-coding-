from my_mod import random as rmod 

human_choice = int(input("choice number 1 - 3: 1 for Rock, 2 for Paper 3 for Scissors\n: "))
computer_choice = rmod.randint(0, 2)

game_text_image = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) ''', '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

 ''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) ''',]


if human_choice == 1 and computer_choice == 0 :
    print(f"\t\n Draw \n your hand { game_text_image[human_choice-1]} \n computer {game_text_image [computer_choice]}")
if human_choice == 1 and computer_choice == 1 : 
    print(f"\t\n Computer wins \n your hand{game_text_image[human_choice-1]}  \n computer {game_text_image [computer_choice]} ")
if human_choice == 1 and computer_choice == 2 :
    print(f"\t You win  \n your hand {game_text_image[human_choice-1]} \n computer {game_text_image [computer_choice]}")

if human_choice == 2 and computer_choice == 1 :
    print(f"\t\n Draw  \n your hand{game_text_image[human_choice-1]}  \n computer {game_text_image [computer_choice]}")
if human_choice == 2 and computer_choice == 0 :
    print(f"\t\n You won  \n your hand{game_text_image[human_choice-1]}  \n computer {game_text_image [computer_choice]}")
if human_choice == 2 and computer_choice == 2: 
    print(f"\t\n Computer wins  \n your hand{game_text_image[human_choice-1]} \n computer {game_text_image [computer_choice]}")

if human_choice == 3 and computer_choice == 2 :
    print(f"\t\n Draw \n your hand {game_text_image[human_choice-1]}  \n computer {game_text_image [computer_choice]}")
if human_choice == 3 and computer_choice == 0:
    print(f"\t\n Computer wins \n your hand {game_text_image[human_choice-1]} \n computer {game_text_image [computer_choice]}")
if human_choice == 3 and computer_choice == 1: 
    print(f"\t\n You win \n your hand {game_text_image[human_choice-1]} \n computer {game_text_image [computer_choice]}")