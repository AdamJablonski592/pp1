def occurs(number, array):
    if number in array:
        return True
    else:
        return False
    
nums = [15, 38, 7, 23, 14]
q = int(input("Number: "))
print(occurs(q, nums))