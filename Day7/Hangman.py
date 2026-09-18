import random as ran
import helper as hp
 
words = [
    # Animals & Nature
    "badger", "cheetah", "dolphin", "falcon", "gorilla", "hedgehog",
    "iguana", "jaguar", "kangaroo", "leopard", "mongoose", "octopus",
    "panther", "quokka", "raccoon", "seagull", "toucan", "vulture",
    "walrus", "canyon", "glacier", "meadow", "plateau", "volcano",

    # Objects & Everyday Things
    "backpack", "compass", "dynamo", "envelope", "flashlight", "harmonica",
    "journal", "kettle", "lantern", "magnet", "notebook", "pendulum",
    "telescope", "umbrella", "whistle", "xylophone",

    # Tricky & Classic Hangman Words (low vowel count or rare letters)
    "abyss", "awkward", "banjo", "blizzard", "buzzard", "cobweb",
    "crypt", "dwarves", "espionage", "fishhook", "fjord", "galaxy",
    "gazebo", "glyph", "haiku", "haphazard", "hyphen", "icebox",
    "jackpot", "jigsaw", "jinx", "kazoo", "keyhole", "khaki",
    "klutz", "matrix", "mnemonic", "mystify", "oxygen", "pajama",
    "pixel", "pneumonia", "puzzling", "quartz", "quiver", "rhythm",
    "scratch", "sphinx", "subway", "swivel", "syndrome", "thrift",
    "unknown", "vaporize", "vortex", "waltz", "whiskey", "wizard",
    "yacht", "zephyr", "zigzag", "zombie"
]

pick_random_word = ran.choice(words)
display = ""
mainloop = True
correct_letter = []

print(pick_random_word)
for word in pick_random_word:
    display += "_"
    
print(display)

while mainloop:
    display = ""
    guess  = input("Guess the letter in the word: ").lower()
    
    for letter in pick_random_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter 
        else:
            display += "_"

    print(display)
    if "_" not in display:
        mainloop = False
        print("You win")
