#user inputs
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

#bmi calculation
bmi = round(weight / height**2 * 10000)

print(f"BMI index is {bmi}")