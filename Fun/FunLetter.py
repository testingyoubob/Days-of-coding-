from helper import time 
from helper import string

letters = list(string.ascii_lowercase + string.ascii_uppercase + ' !')

target = "Hello World!"

current_str = ""

while current_str != target:
    for letter in letters:
        print(f"\r{current_str + letter} ", end="", flush=True)
        time.sleep(0.01)

        if current_str + letter == target[:len(current_str)+1]:
            current_str += letter
            break

        print(f"\r{current_str}", end="", flush=True)
print(f"\r{target}")