import os
import random
os.system('clear')

def question():
    if raw_input("Would you like to roll again? Y/N ") == 'Y':
        os.system('clear')
        dice()
    else:
        os.system('clear')
        print("Goodbye!")

def dice():
    print random.randint(1, 6)
    question()
dice()
