import math
amount = int(input("Enter the amount in PLN: "))

fives = math.floor(amount / 5)
twos = math.floor((amount - (fives * 5)) / 2)
ones = amount - (twos * 2) - (fives * 5)

print(f"5 zł - {fives}")
print(f"2 zł - {twos}")
print(f"1 zł - {ones}")