import random
nums = [1, 52, 12, 32, 55, 4, 6]
def rand_elem(array):
    rand_elements = []
    for i in range(3):
        choice = random.choice(array)
        rand_elements.append(choice)
    return rand_elements

print(rand_elem(nums))