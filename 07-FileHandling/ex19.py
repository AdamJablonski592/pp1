with open('integers.txt', 'w') as f:
    for num in range(1, 51):
        num_str = str(num)
        if num == 50:
            f.write(num_str)
        else:
            f.write(num_str)
            f.write("\n")