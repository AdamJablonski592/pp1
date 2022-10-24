import random

def read_number():
    return int(input("Enter your guess: "))

def generate_number():
    return random.randint(1,9)