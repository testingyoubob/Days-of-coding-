loop = True 
while loop:

    try:
        a = int(input("Input a whole number to divide by: "))
        b = int(input("Input a second whole number to divide by: "))
        divided = a / b 
        
    except ZeroDivisionError as e: 
        print(str(e))
        print("Can't Divide by zero")
    except ValueError:
        print("Input Errors! Needs to be numbers Try again.")
    else: 
        print(f" Your answer is {divided} ")
        again = input("Would you like to try again? y/n :")
        if again == "y":
            continue
        elif again == "n":
            break 
        else:
            print("Needs to be y for yes n for no restart the program")
            break