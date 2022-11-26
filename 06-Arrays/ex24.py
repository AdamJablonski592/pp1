nums = [1, 5, 125, 22, 13]
q = int(input("Enter a number: "))
elements = 0

for num in nums:
    if num > q:
        elements += 1
    else:
        continue
    
print(elements)