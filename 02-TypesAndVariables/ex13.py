#determine radius and PI
RADIUS = 5
PI = 3.14

#calculate area
def calculate_area():
    return round(PI * RADIUS**2, 2)

#calculate circumference
def calculate_circumference():
    return round(2*PI*RADIUS, 2)

#display results
print(f"The circle's area is {calculate_area()} and its circumference is {calculate_circumference()}")
