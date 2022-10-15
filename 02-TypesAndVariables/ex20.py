import random

#dice variables
dice_rolls = []
dice_values = 0

#generating dice numbers
for i in range(0,3):
    roll = random.randint(1,6)
    dice_values += roll
    dice_rolls.append(roll)
    
print(f"The rolled numbers are {dice_rolls} and their value is {dice_values}")