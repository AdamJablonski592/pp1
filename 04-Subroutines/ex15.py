import mymath as m

guess = m.read_number()
computer_guess = m.generate_number()

if guess == computer_guess:
    print("You guessed")
else:
    print(f"Wrong guess. Computer's guess is {computer_guess}")