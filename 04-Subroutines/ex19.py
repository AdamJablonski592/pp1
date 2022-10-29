def within_range(x, y, num):
    if num >= x and num <= y:
        return True
    else:
        return False

x = int(input("Enter the first range: "))
y = int(input("Enter the second range:"))
num = int(input("Enter the number: "))
print(within_range(x, y, num))