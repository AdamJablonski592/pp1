height = int(input("Enter the height of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

for i in range(1, height + 1):
    for j in range(1, width + 1):
        if i == 1 or i == height or j == 1 or j == width:
            print("*", end="")
        else:
            print(" ", end="")
    print("\n")
