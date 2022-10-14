int = 4
str = "The value is {number}, and its second power is {second_power}"

print(str.format(number=int, second_power=int**2))