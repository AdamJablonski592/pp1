#user input
height = int(input("What is your height?: "))

#feet and inches calculation
feet = int(height/30.48)
inches = round((height - (feet * 30.48)) / 2.54, 2)

print(f"I am {height} cm tall, i.e. {feet} feet and {inches} inches")