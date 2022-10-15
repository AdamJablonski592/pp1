#user input
celsius = float(input("Enter temperature in Celcius: "))

#degrees calculation
fahrenheit = (celsius * (9/5)) + 32
kelvin = celsius + 273.15

print(f"{celsius}°C equals to {fahrenheit}°F and {kelvin}°K")