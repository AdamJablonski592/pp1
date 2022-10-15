import math

#user inputs
a = float(input("Input the first value (a): "))
b = float(input("Input the second value (b): "))
c = float(input("Input the third value (c): "))

#Heron formula
s = (a + b + c) / 2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(f"The area of a tringle is {area}")