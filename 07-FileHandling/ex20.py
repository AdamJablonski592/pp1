import random

with open('random_int.txt', 'w') as f:
    for i in range(1, 51):
        rand_num = random.randint(100, 999)
        rand_num_str = str(rand_num)
        
        if i == 50:
            f.write(rand_num_str)
        else:
            f.write(rand_num_str)
            f.write("\n")