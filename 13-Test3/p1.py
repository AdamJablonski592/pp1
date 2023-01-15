def f(n):
    for i in range(n):
        if i % 5 == 0 and i != 0:
            print("-", end="")
            print("/", end="")
        else:
            print("/", end="")
        
f(11)