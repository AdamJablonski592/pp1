quantity = 0
sum = 0
mean = 0
is_running = True

while is_running:
    num = int(input("Enter number: "))
    quantity += 1
    sum += num
    
    if num == 0:
        quantity -= 1
        mean = sum/quantity
        print(f"RESULT: Quantity={quantity}, Sum={sum}, Mean={mean}")
        is_running = False