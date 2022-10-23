terms = int(input("Enter the amount of terms: "))

n1, n2 = 0, 1
count = 0
is_running = True

while is_running:
    if terms <= 0:
        print("Invalid input")
        terms = int(input("Enter the amount of terms: "))
    elif terms == 1:
        print(f"Fibonacci sequence: {n1}")
        is_running = False
    else:
        print("Fibonacci sequence: ")
        while count < terms:
            print(n1)
            next_term = n1 + n2
            n1 = n2
            n2 = next_term
            count += 1
        is_running = False
