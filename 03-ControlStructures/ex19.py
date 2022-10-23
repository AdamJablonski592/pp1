human_years = int(input("Enter the dog's age in human years: "))

if human_years <= 0:
    print("Invalid input")
elif human_years <= 2:
    age = human_years * 10.5
    print(f"The dog's age in dog's years is {age} years")
else:
    age = 21 + (human_years - 2) * 4
    print(f"The dog's age in dog's years is {age} years")