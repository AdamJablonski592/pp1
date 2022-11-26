nums = [2, 532, 11, 55, 3]
even = 0
odd = 0
for num in nums:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
        
print(even, odd)
