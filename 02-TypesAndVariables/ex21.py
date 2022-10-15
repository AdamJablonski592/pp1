import random

#computer and player choices
computer_choice = random.randint(1,6)
guess = int(input("Guess the computer's number from a dice: "))

#program logic
if guess == computer_choice:
    print("True")
else:
    print("False")